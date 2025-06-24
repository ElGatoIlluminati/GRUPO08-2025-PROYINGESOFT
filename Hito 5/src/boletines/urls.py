from django.urls import path
from . import views

app_name = 'boletines'

urlpatterns = [
    # Rutas para listar y ver detalles
    path('', views.BoletinListView.as_view(), name='lista'),
    path('<int:pk>/', views.BoletinDetailView.as_view(), name='detalle'),

    # Rutas CRUD (Crear, Editar, Eliminar)
    path('crear/', views.BoletinCreateView.as_view(), name='crear'),
    
    # Aquí está la corrección: Usamos la nueva Clase 'BoletinUpdateView'
    path('<int:pk>/editar/', views.BoletinUpdateView.as_view(), name='editar'),
    
    path('<int:pk>/eliminar/', views.BoletinDeleteView.as_view(), name='eliminar'),

    # Rutas de funcionalidades adicionales
    path('enviar-email/<int:pk>/', views.enviar_boletin_email_view, name='enviar_email'),
    path('pdf-preview/<int:pk>/', views.pdf_preview_view, name='pdf_preview'),
]
