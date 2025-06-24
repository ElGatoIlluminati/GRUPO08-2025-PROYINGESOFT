# src/users/urls.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # ej: http://localhost:8000/cuentas/login/
    path('login/', views.login_view, name='login'),
    # ej: http://localhost:8000/cuentas/logout/
    path('logout/', views.logout_view, name='logout'),
    # ej: http://localhost:8000/cuentas/registro/
    path('registro/', views.register_view, name='registro'),
    # ej: http://localhost:8000/cuentas/perfil/
    path('perfil/', views.perfil_view, name='perfil'),
    # ej: http://localhost:8000/cuentas/perfil/editar/
    path('perfil/editar/', views.perfil_editar_view, name='perfil_editar'),
    # ej: http://localhost:8000/cuentas/perfil/eliminar/
    path('eliminar-cuenta/', views.UserDeleteView.as_view(), name='user_delete'),
]