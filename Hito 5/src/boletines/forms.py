# src/boletines/forms.py
from django import forms
from .models import Boletin

class BoletinForm(forms.ModelForm):
    class Meta:
        model = Boletin
        # Incluimos todos los campos que queremos en el formulario
        fields = ['title', 'category', 'tags', 'photo', 'document']
        labels = {
            'title': 'Título del Boletín',
            'category': 'Categoría',
            'tags': 'Etiquetas (puedes seleccionar varias manteniendo presionado Ctrl o Cmd)',
            'photo': 'Foto de Portada (opcional)',
            'document': 'Documento PDF del Boletín',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Este bucle añade la clase 'form-control' de Bootstrap a cada campo
        # para que se estilicen correctamente de forma automática.
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxSelectMultiple):
                # Las etiquetas múltiples no usan form-control, se estilizan diferente
                field.widget.attrs.update({'class': 'form-check'})
            elif isinstance(field.widget, forms.SelectMultiple):
                 field.widget.attrs.update({'class': 'form-select', 'size': '5'})
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})