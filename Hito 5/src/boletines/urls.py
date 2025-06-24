from django.urls import path
from . import views

# El app_name nos ayuda a organizar las URLs y a llamarlas fácilmente desde las plantillas
app_name = 'boletines'

urlpatterns = [
    # Ruta para la página de inicio/lista de boletines
    # ej: http://localhost:8000/
    path('', views.BoletinListView.as_view(), name='lista'),

    # Ruta para ver el detalle de un boletín
    # ej: http://localhost:8000/boletines/5/
    path('<int:pk>/', views.BoletinDetailView.as_view(), name='detalle'),
    
    #   Ruta para la vista previa del PDF
    path('<int:pk>/preview/', views.pdf_preview_view, name='pdf_preview'),

    # Ruta para crear un nuevo boletín
    # ej: http://localhost:8000/boletines/crear/
    path('crear/', views.BoletinCreateView.as_view(), name='crear'),

    # Ruta para editar un boletín existente
    # ej: http://localhost:8000/boletines/5/editar/
    path('<int:pk>/editar/', views.BoletinUpdateView.as_view(), name='editar'),

    # Ruta para eliminar un boletín
    # ej: http://localhost:8000/boletines/5/eliminar/
    path('<int:pk>/eliminar/', views.BoletinDeleteView.as_view(), name='eliminar'),


    # NUEVA RUTA para la generación con IA
    path('generar/', views.generar_boletin_view, name='generar'),
]