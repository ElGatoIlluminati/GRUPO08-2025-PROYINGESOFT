# src/users/apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # AÑADIMOS ESTE MÉTODO
    def ready(self):
        import users.signals  # Importa y conecta las señales