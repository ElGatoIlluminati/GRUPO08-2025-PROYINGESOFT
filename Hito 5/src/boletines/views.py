from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.http import FileResponse, HttpResponse
from .models import Boletin
from .forms import BoletinForm 

# Create your views here.

# Vista para listar todos los boletines (nuestra página de inicio)
class BoletinListView(ListView):
    model = Boletin
    template_name = 'boletines.html'  # Usará la plantilla que ya tienes
    context_object_name = 'boletines' # Nombre de la variable en la plantilla
    ordering = ['-creation_date'] # Ordenar del más nuevo al más antiguo

# Vista para ver el detalle de un solo boletín
class BoletinDetailView(DetailView):
    model = Boletin
    template_name = 'boletin_detalle.html' # Necesitarás crear esta plantilla
    context_object_name = 'boletin'

# Vista para crear un nuevo boletín
class BoletinCreateView(LoginRequiredMixin, CreateView):
    model = Boletin
    form_class = BoletinForm      # <--- 2. USA form_class EN LUGAR DE 'fields'
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
    template_name = 'boletin_confirmar_eliminar.html' # Necesitarás crear esta plantilla
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