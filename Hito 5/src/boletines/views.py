# Hito 5/src/boletines/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import FileResponse, HttpResponse

from .models import Boletin
from .forms import BoletinForm

# --- VISTAS PARA LISTAR Y VER DETALLES DE BOLETINES ---

class BoletinListView(ListView):
    """Muestra la lista de todos los boletines con filtros."""
    model = Boletin
    template_name = 'boletines/boletin_list.html'
    context_object_name = 'boletines'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-creation_date')
        search_query = self.request.GET.get('q', None)
        fecha_desde = self.request.GET.get('fecha_desde', None)
        fecha_hasta = self.request.GET.get('fecha_hasta', None)

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        if fecha_desde:
            queryset = queryset.filter(creation_date__date__gte=fecha_desde)
        if fecha_hasta:
            queryset = queryset.filter(creation_date__date__lte=fecha_hasta)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_search'] = self.request.GET.get('q', '')
        context['current_fecha_desde'] = self.request.GET.get('fecha_desde', '')
        context['current_fecha_hasta'] = self.request.GET.get('fecha_hasta', '')
        return context

class BoletinDetailView(DetailView):
    """Muestra la página de detalle de un único boletín."""
    model = Boletin
    template_name = 'boletines/boletin_detalle.html'
    context_object_name = 'boletin'


# --- VISTAS PARA CREAR, EDITAR Y ELIMINAR BOLETINES (CRUD) ---

# Un mixin para reutilizar la lógica de permisos
class StaffEditorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or (hasattr(self.request.user, 'userprofile') and self.request.user.userprofile.role in ['admin', 'editor'])

class BoletinCreateView(StaffEditorRequiredMixin, CreateView):
    """Permite a usuarios autorizados crear un nuevo boletín."""
    model = Boletin
    form_class = BoletinForm
    template_name = 'boletines/crear_boletin.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "El boletín ha sido creado con éxito.")
        return super().form_valid(form)

# ESTA VISTA REEMPLAZA A editar_boletin_view y a la BoletinUpdateView antigua.
class BoletinUpdateView(StaffEditorRequiredMixin, UpdateView):
    """Permite a usuarios autorizados editar un boletín existente."""
    model = Boletin
    form_class = BoletinForm
    template_name = 'boletines/editar_boletin.html'
    context_object_name = 'boletin'

    def form_valid(self, form):
        form.instance.last_edit_by = self.request.user
        messages.success(self.request, f'El boletín "{self.get_object().title}" ha sido actualizado con éxito.')
        return super().form_valid(form)

class BoletinDeleteView(StaffEditorRequiredMixin, DeleteView):
    """Permite a usuarios autorizados eliminar un boletín."""
    model = Boletin
    template_name = 'boletines/boletin_confirmar_eliminar.html'
    success_url = reverse_lazy('boletines:lista')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, f'El boletín "{self.get_object().title}" ha sido eliminado.')
        return super().post(request, *args, **kwargs)


# --- VISTAS DE FUNCIONALIDADES ADICIONALES ---

@login_required
def enviar_boletin_email_view(request, pk):
    """Maneja la lógica para enviar un boletín por correo electrónico."""
    if request.method == 'POST':
        boletin = get_object_or_404(Boletin, pk=pk)
        usuario = request.user

        # Usamos el nuevo nombre del campo: pdf_file
        if not boletin.pdf_file:
            messages.error(request, "Este boletín no tiene un documento PDF para enviar.")
        elif not usuario.email:
            messages.error(request, "Tu perfil no tiene una dirección de correo para recibir el boletín.")
        else:
            try:
                asunto = f"Tu Boletín VIGIFIA: {boletin.title}"
                cuerpo = f"Hola {usuario.first_name or usuario.username},\n\nAdjuntamos el boletín '{boletin.title}' que solicitaste."
                
                email = EmailMessage(
                    subject=asunto,
                    body=cuerpo,
                    from_email='VIGIFIA <grupo8ingesoftvigifia@gmail.com>',
                    to=[usuario.email]
                )
                
                boletin.pdf_file.open(mode='rb')
                email.attach(f'{boletin.title}.pdf', boletin.pdf_file.read(), 'application/pdf')
                boletin.pdf_file.close()
                
                email.send()
                messages.success(request, f"¡El boletín ha sido enviado a tu correo: {usuario.email}!")

            except Exception as e:
                messages.error(request, f"Ocurrió un error al intentar enviar el correo: {e}")
            
    return redirect('boletines:detalle', pk=pk)

def pdf_preview_view(request, pk):
    """Vista para la previsualización segura de PDF en iframes."""
    boletin = get_object_or_404(Boletin, pk=pk)
    
    # Usamos el nuevo nombre del campo: pdf_file
    if not boletin.pdf_file:
        return HttpResponse("Documento no encontrado.", status=404)

    try:
        response = FileResponse(boletin.pdf_file.open('rb'), content_type='application/pdf')
        # Esta cabecera es importante para la seguridad
        response['Content-Security-Policy'] = "frame-ancestors 'self'"
        return response
    except FileNotFoundError:
        return HttpResponse("Archivo no encontrado en el servidor.", status=404)
