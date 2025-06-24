from django import forms
from .models import Boletin
from django_summernote.widgets import SummernoteWidget

class BoletinForm(forms.ModelForm):
    class Meta:
        model = Boletin
        fields = ['title', 'description', 'pdf_file', 'photo', 'category']
        widgets = { 'description': SummernoteWidget(), }
        labels = {
            'title': 'Nombre del Boletín',
            'description': 'Descripción',
            'pdf_file': 'Archivo PDF (opcional)',
            'photo': 'Imagen de portada (opcional)',
            'category': 'Categoría'
        }