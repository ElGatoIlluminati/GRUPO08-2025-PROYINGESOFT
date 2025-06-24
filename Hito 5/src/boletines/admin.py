# src/boletines/admin.py
from django.contrib import admin
from .models import Boletin, Categoria, Tag

admin.site.register(Boletin)
admin.site.register(Categoria)
admin.site.register(Tag)