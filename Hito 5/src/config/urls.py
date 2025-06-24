"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # El admin de Django por defecto

    # URL "secreta" para panel personalizado
    path('gestion-secreta/', include('dashboard.urls')),
    # Cualquier URL que empiece con 'boletines/' será manejada por la app 'boletines'
    path('boletines/', include('boletines.urls')),
    # Cualquier URL de cuentas (login, logout, etc.) será manejada por la app 'users'
    path('cuentas/', include('users.urls')),

    # La ruta raíz ahora la maneja la app 'core'
    path('', include('core.urls')),
]

# Esto es para servir archivos de media (subidos por usuarios) en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)