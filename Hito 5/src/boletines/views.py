from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.http import FileResponse, HttpResponse
from django.core.mail import EmailMessage
from .models import Boletin
from .forms import BoletinForm 

# Create your views here.

# Vista para listar todos los boletines
class BoletinListView(ListView):
    model = Boletin
    template_name = 'boletines/boletin_list.html'
    context_object_name = 'boletines'
    paginate_by = 9 # Opcional: Muestra 9 boletines por página

    def get_queryset(self):
        """
        Sobrescribimos este método para añadir la lógica de filtro.
        """
        queryset = super().get_queryset().order_by('-creation_date')
        
        # Obtenemos los parámetros de la URL
        search_query = self.request.GET.get('q', None)
        fecha_desde = self.request.GET.get('fecha_desde', None)
        fecha_hasta = self.request.GET.get('fecha_hasta', None)

        # Aplicamos los filtros si existen
        if search_query:
            # Filtra por título que contenga el texto de búsqueda (insensible a mayúsculas)
            queryset = queryset.filter(title__icontains=search_query)
        
        if fecha_desde:
            # Filtra por fecha de creación mayor o igual a la fecha "desde"
            queryset = queryset.filter(creation_date__date__gte=fecha_desde)

        if fecha_hasta:
            # Filtra por fecha de creación menor o igual a la fecha "hasta"
            queryset = queryset.filter(creation_date__date__lte=fecha_hasta)
            
        return queryset

    def get_context_data(self, **kwargs):
        """
        Pasamos los valores actuales del filtro de vuelta a la plantilla
        para que los campos de búsqueda no se borren después de enviar.
        """
        context = super().get_context_data(**kwargs)
        context['current_search'] = self.request.GET.get('q', '')
        context['current_fecha_desde'] = self.request.GET.get('fecha_desde', '')
        context['current_fecha_hasta'] = self.request.GET.get('fecha_hasta', '')
        return context

# Vista para ver el detalle de un solo boletín
class BoletinDetailView(DetailView):
    model = Boletin
    template_name = 'boletines/boletin_detalle.html' # Necesitarás crear esta plantilla
    context_object_name = 'boletin'

# Vista para crear un nuevo boletín
class BoletinCreateView(LoginRequiredMixin, CreateView):
    model = Boletin
    form_class = BoletinForm      # <--- 2. Usa form_class EN LUGAR DE 'fields'
    template_name = 'boletines/crear_boletin.html' # Usaremos una nueva ruta de plantilla
    success_url = reverse_lazy('boletines:lista')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Vista para actualizar un boletín
class BoletinUpdateView(LoginRequiredMixin, UpdateView):
    model = Boletin
    form_class = BoletinForm      # <--- 3. APLICA EL MISMO CAMBIO AQUÍ
    template_name = 'boletines/editar_boletin.html' # Usaremos una nueva ruta
    success_url = reverse_lazy('boletines:lista')

    def form_valid(self, form):
        form.instance.last_edit_by = self.request.user
        return super().form_valid(form)

# Vista para eliminar un boletín
class BoletinDeleteView(LoginRequiredMixin, DeleteView):
    model = Boletin
    template_name = 'boletines/boletin_confirmar_eliminar.html' # Necesitarás crear esta plantilla
    success_url = reverse_lazy('boletines:lista')


@login_required # Protegemos para que solo usuarios logueados puedan acceder
def generar_boletin_view(request):
    # Por ahora, esta vista no hace nada más que mostrar la página.
    # En el futuro, aquí irá la lógica de scraping y IA.
    if request.method == 'POST':
        # Aquí procesaremos los datos del formulario
        titulo = request.POST.get('titulo')
        tema = request.POST.get('tema')
        descripcion = request.POST.gret('descripcion')

        # TODO: Llamar a la función de scraping
        # TODO: Llamar a la API de la IA
        # TODO: Llamar a la función que crea el .docx
        # TODO: Redirigir al editor WYSIWYG

        messages.info(request, f"Procesando solicitud para el boletín: {titulo}")
        return redirect('boletines:lista') # Redirigimos a la lista por ahora

    return render(request, 'boletines/generar_boletin.html')

# Para la previsualización segura de PDF
def pdf_preview_view(request, pk):
    boletin = get_object_or_404(Boletin, pk=pk)
    if not boletin.document:
        return HttpResponse("Documento no encontrado.", status=404)

    try:
        # Creamos una respuesta de archivo para enviar el PDF
        response = FileResponse(boletin.document.open('rb'), content_type='application/pdf')

        # ¡LA LÍNEA CLAVE! Esta cabecera le da permiso al navegador para mostrar el PDF en un iframe
        # 'self' significa que solo se permite si la página principal es del mismo origen (tu propio sitio)
        response['Content-Security-Policy'] = "frame-ancestors 'self'"

        return response
    except FileNotFoundError:
        return HttpResponse("Archivo no encontrado en el servidor.", status=404)
    
# Vista para manejar el envío de correos
@login_required
def enviar_boletin_email_view(request, pk):
    # Usamos POST para que esta acción no se pueda ejecutar accidentalmente
    if request.method == 'POST':
        boletin = get_object_or_404(Boletin, pk=pk)
        usuario = request.user

        if not boletin.document:
            messages.error(request, "Este boletín no tiene un documento para enviar.")
            return redirect('boletines:detalle', pk=boletin.pk)

        if not usuario.email:
            messages.error(request, "Tu perfil no tiene una dirección de correo electrónico para recibir el boletín.")
            return redirect('boletines:detalle', pk=boletin.pk)

        try:
            # Construimos el correo
            asunto = f"Tu Boletín VIGIFIA: {boletin.title}"
            cuerpo = f"Hola {usuario.first_name or usuario.username},\n\nAdjuntamos el boletín '{boletin.title}' que solicitaste.\n\n¡Gracias por usar VIGIFIA!"

            email = EmailMessage(
                subject=asunto,
                body=cuerpo,
                from_email='VIGIFIA <grupo8ingesoftvigifia@gmail.com>', # Remitente
                to=[usuario.email] # Destinatario
            )

            # Adjuntamos el archivo PDF
            boletin.document.open() # Abrimos el archivo
            email.attach(f'{boletin.title}.pdf', boletin.document.read(), 'application/pdf')
            boletin.document.close() # Lo cerramos

            # Enviamos el correo (en nuestro caso, lo imprimirá en la consola)
            email.send()

            messages.success(request, f"¡El boletín ha sido enviado a tu correo: {usuario.email}!")

        except Exception as e:
            messages.error(request, f"Ocurrió un error al intentar enviar el correo: {e}")

    # Redirigimos siempre a la página de detalle
    return redirect('boletines:detalle', pk=pk)