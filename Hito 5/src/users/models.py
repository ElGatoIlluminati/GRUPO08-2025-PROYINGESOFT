from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Administrador', 'Administrador'),
        ('Editor', 'Editor'),
        ('Lector', 'Lector'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='Lector')

    def __str__(self):
        return f"{self.user.username} - {self.role}"