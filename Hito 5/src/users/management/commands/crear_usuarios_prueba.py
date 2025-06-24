import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files import File
from boletines.models import Boletin, Categoria

class Command(BaseCommand):
    help = 'Crea usuarios y datos de prueba completos (categorías, boletines con archivos) para la revisión.'

    def handle(self, *args, **options):
        User = get_user_model()
        self.stdout.write(self.style.SUCCESS('--- Iniciando la creación de datos de prueba ---'))

        # --- 1. Creación de Categorías ---
        self.stdout.write('Creando categorías...')
        cat_clima, _ = Categoria.objects.get_or_create(nombre='Cambio Climático')
        cat_mercado, _ = Categoria.objects.get_or_create(nombre='Mercado y Tendencias')
        self.stdout.write(self.style.SUCCESS('Categorías creadas.'))

        # --- 2. Creación de Usuarios ---
        self.stdout.write('Creando usuarios de prueba...')
        # (El código para crear usuarios no cambia)
        users_to_create = [
            {'username': 'admin', 'password': 'admin123', 'is_staff': True, 'is_superuser': True, 'role': 'admin'},
            {'username': 'editor', 'password': 'editor123', 'is_staff': False, 'is_superuser': False, 'role': 'editor'},
            {'username': 'lector', 'password': 'lector123', 'is_staff': False, 'is_superuser': False, 'role': 'lector'},
        ]
        for user_data in users_to_create:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
                user.is_staff = user_data['is_staff']
                user.is_superuser = user_data['is_superuser']
                user.save()
                user.userprofile.role = user_data['role']
                user.userprofile.save()
                self.stdout.write(self.style.SUCCESS(f" > Usuario '{user_data['username']}' creado."))
        self.stdout.write(self.style.SUCCESS('Usuarios creados.'))