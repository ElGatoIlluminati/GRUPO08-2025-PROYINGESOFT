# Hito 5/src/users/management/commands/crear_usuarios_prueba.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from boletines.models import Boletin, Categoria

class Command(BaseCommand):
    help = 'Crea usuarios y datos de prueba (categorías, boletines) para la revisión del proyecto.'

    def handle(self, *args, **options):
        User = get_user_model()
        self.stdout.write(self.style.SUCCESS('--- Iniciando la creación de datos de prueba ---'))

        # --- 1. Creación de Categorías ---
        self.stdout.write('Creando categorías...')
        cat_clima, _ = Categoria.objects.get_or_create(nombre='Cambio Climático')
        cat_mercado, _ = Categoria.objects.get_or_create(nombre='Mercado y Tendencias')
        self.stdout.write(self.style.SUCCESS('Categorías creadas.'))

        # --- 2. Creación de Usuarios ---
        users_to_create = [
            {'username': 'admin', 'password': 'admin123', 'is_staff': True, 'is_superuser': True, 'role': 'admin'},
            {'username': 'editor', 'password': 'editor123', 'is_staff': False, 'is_superuser': False, 'role': 'editor'},
            {'username': 'lector', 'password': 'lector123', 'is_staff': False, 'is_superuser': False, 'role': 'lector'},
        ]
        self.stdout.write('Creando usuarios de prueba...')
        for user_data in users_to_create:
            if User.objects.filter(username=user_data['username']).exists():
                self.stdout.write(self.style.WARNING(f"Usuario '{user_data['username']}' ya existe. Saltando."))
                continue
            user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
            user.is_staff = user_data['is_staff']
            user.is_superuser = user_data['is_superuser']
            user.save()
            user.userprofile.role = user_data['role']
            user.userprofile.save()
            self.stdout.write(self.style.SUCCESS(f" > Usuario '{user_data['username']}' creado."))
        self.stdout.write(self.style.SUCCESS('Usuarios creados.'))

        # --- 3. Creación de Boletines de Ejemplo ---
        self.stdout.write('Creando boletines de ejemplo...')
        admin_user = User.objects.get(username='admin')
        
        Boletin.objects.get_or_create(
            title='Informe sobre Adaptación al Cambio Climático',
            author=admin_user,
            defaults={
                'category': cat_clima,
                'description': '<p>Este es un informe detallado sobre las nuevas estrategias de adaptación al cambio climático en el sector agrícola.</p>'
            }
        )
        Boletin.objects.get_or_create(
            title='Análisis de Tendencias del Mercado Agroalimentario',
            author=admin_user,
            defaults={
                'category': cat_mercado,
                'description': '<h3>Resumen Ejecutivo</h3><p>El mercado muestra una fuerte tendencia hacia productos orgánicos y sostenibles.</p>'
            }
        )
        self.stdout.write(self.style.SUCCESS('Boletines de ejemplo creados.'))

        self.stdout.write(self.style.SUCCESS('--- Proceso de creación de datos de prueba finalizado ---'))
