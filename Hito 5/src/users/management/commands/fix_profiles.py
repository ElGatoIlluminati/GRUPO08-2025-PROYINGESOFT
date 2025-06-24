from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile

class Command(BaseCommand):
    help = 'Asegura que cada usuario tenga un UserProfile con un rol por defecto.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE('Iniciando proceso para arreglar perfiles...'))
        
        usuarios_sin_perfil = User.objects.filter(userprofile__isnull=True)
        
        if not usuarios_sin_perfil.exists():
            self.stdout.write(self.style.SUCCESS('¡Excelente! Todos los usuarios ya tienen un perfil.'))
            return

        self.stdout.write(f'Se encontraron {usuarios_sin_perfil.count()} usuarios sin perfil.')

        for usuario in usuarios_sin_perfil:
            # Determinamos el rol por defecto
            rol_defecto = 'Administrador' if usuario.is_superuser else 'Lector'
            
            # Usamos get_or_create para ser seguros
            perfil, creado = UserProfile.objects.get_or_create(
                user=usuario,
                defaults={'role': rol_defecto}
            )

            if creado:
                self.stdout.write(self.style.SUCCESS(f'Perfil creado para "{usuario.username}" con el rol "{rol_defecto}".'))
            else:
                self.stdout.write(self.style.WARNING(f'El perfil para "{usuario.username}" ya existía, no se hizo nada.'))
        
        self.stdout.write(self.style.NOTICE('Proceso finalizado.'))