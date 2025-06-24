from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # RUTA PRINCIPAL
    path('', views.dashboard_home_view, name='home'),
    # La vista principal del dashboard será la lista de usuarios
    path('usuarios/', views.user_list_view, name='user_list'),
    # Una ruta para manejar la actualización del rol
    path('usuarios/actualizar-rol/', views.update_user_role, name='update_user_role'),
    # Para la página de confirmación de borrado de usuario
    path('usuarios/<int:pk>/eliminar/', views.UserDeleteView.as_view(), name='user_delete'),

    path('categorias/', views.manage_categories_view, name='manage_categories'),
    path('categorias/<int:pk>/eliminar/', views.delete_category_view, name='delete_category'),
]