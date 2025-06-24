from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Boletin, Categoria

class BoletinAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'author', 'category', 'creation_date', 'last_edit_date')
    list_filter = ('category', 'creation_date')
    search_fields = ('title', 'description')

admin.site.register(Boletin, BoletinAdmin)
admin.site.register(Categoria)