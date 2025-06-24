from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Tag(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Boletin(models.Model):
    photo = models.ImageField(upload_to='boletines_photos/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    document = models.FileField(upload_to='boletines_docs/', null=True, blank=True)
    author = models.ForeignKey(User, related_name='created_boletins', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_by = models.ForeignKey(User, related_name='edited_boletins', on_delete=models.SET_NULL, null=True, blank=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title or "Boletín sin título"