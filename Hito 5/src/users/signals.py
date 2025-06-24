# src/users/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Esta función se ejecuta cada vez que un objeto User se guarda.
    Si el usuario es nuevo (created=True), le crea un perfil.
    Si el usuario ya existe, actualiza el rol si es necesario.
    """
    profile, profile_created = UserProfile.objects.get_or_create(user=instance)

    # Si el usuario es un superusuario y su rol no es 'Administrador', se lo asignamos.
    if instance.is_superuser and profile.role != 'Administrador':
        profile.role = 'Administrador'
        profile.save()
    # Si el perfil se acaba de crear y no es superusuario, por defecto será 'Lector'
    # (esto ya lo maneja el 'default' del modelo, pero es bueno ser explícito).
    elif profile_created and not instance.is_superuser:
        profile.role = 'Lector'
        profile.save()