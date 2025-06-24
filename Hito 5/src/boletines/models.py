from django.db import models
from django.conf import settings
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.nombre

class Boletin(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    photo = models.ImageField(upload_to='boletines/portadas/', blank=True, null=True, verbose_name="Portada")
    category = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoría")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='boletines_creados', verbose_name="Autor")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    last_edit_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='boletines_editados', verbose_name="Autor de Última Edición")
    last_edit_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de Última Edición")
    description = models.TextField(verbose_name="Descripción", blank=True)
    pdf_file = models.FileField(upload_to='boletines/pdfs/', blank=True, null=True, verbose_name="Archivo PDF")

    class Meta:
        ordering = ['-creation_date']
        verbose_name = "Boletín"
        verbose_name_plural = "Boletines"

    def __str__(self): return self.title
    def get_absolute_url(self): return reverse('boletines:detalle', kwargs={'pk': self.pk})