from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crea los usuarios de prueba (admin, editor, lector) con sus roles correspondientes.'

    def handle(self, *args, **options):
        User = get_user_model()

        # Datos de los usuarios a crear
        users_to_create = [
            {'username': 'admin', 'password': 'admin123', 'is_staff': True, 'is_superuser': True, 'role': 'admin'},
            {'username': 'editor', 'password': 'editor123', 'is_staff': False, 'is_superuser': False, 'role': 'editor'},
            {'username': 'lector', 'password': 'lector123', 'is_staff': False, 'is_superuser': False, 'role': 'lector'},
        ]

        self.stdout.write(self.style.SUCCESS('Iniciando la creación de usuarios de prueba...'))

        for user_data in users_to_create:
            # Revisa si el usuario ya existe
            if User.objects.filter(username=user_data['username']).exists():
                self.stdout.write(self.style.WARNING(f"El usuario '{user_data['username']}' ya existe. Saltando."))
                continue

            # Crea el usuario
            user = User.objects.create_user(
                username=user_data['username'],
                password=user_data['password']
            )

            # Asigna los permisos especiales y el rol
            user.is_staff = user_data['is_staff']
            user.is_superuser = user_data['is_superuser']
            
            # Asegurarse de que el perfil se guarde
            user.save() 
            
            # Asignar el rol al perfil de usuario
            user.userprofile.role = user_data['role']
            user.userprofile.save()

            self.stdout.write(self.style.SUCCESS(f"Usuario '{user_data['username']}' creado exitosamente con el rol '{user_data['role']}'."))
        
        self.stdout.write(self.style.SUCCESS('Proceso finalizado.'))