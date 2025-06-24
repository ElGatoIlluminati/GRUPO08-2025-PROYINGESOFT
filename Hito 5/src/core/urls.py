# src/core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # La ruta vacía ('') corresponde a la raíz del sitio que se delegue a esta app
    path('', views.home_view, name='home'),
]