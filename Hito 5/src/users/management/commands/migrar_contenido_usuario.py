from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from boletines.models import Boletin

class Command(BaseCommand):
    help = 'Reasigna contenido de un usuario a otro y luego elimina el usuario original.'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # --- CONFIGURACIÓN ---
        usuario_original_username = 'Flan'
        nuevo_dueño_username = 'admin'
        # ---------------------

        self.stdout.write(self.style.SUCCESS(f"Iniciando migración de contenido del usuario '{usuario_original_username}'..."))

        try:
            usuario_original = User.objects.get(username=usuario_original_username)
            nuevo_dueño = User.objects.get(username=nuevo_dueño_username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Error: No se encontró al usuario '{usuario_original_username}' o a '{nuevo_dueño_username}'. Asegúrate de haberlos creado primero."))
            return

        # Reasignar boletines donde es autor
        boletines_como_autor = Boletin.objects.filter(author=usuario_original)
        count_autor = boletines_como_autor.update(author=nuevo_dueño)
        self.stdout.write(f"  > {count_autor} boletines reasignados de 'author'.")

        # Reasignar boletines donde fue el último en editar
        boletines_como_editor = Boletin.objects.filter(last_edit_by=usuario_original)
        count_editor = boletines_como_editor.update(last_edit_by=nuevo_dueño)
        self.stdout.write(f"  > {count_editor} boletines reasignados de 'last_edit_by'.")

        # Eliminar el usuario original
        self.stdout.write(self.style.WARNING(f"Intentando eliminar al usuario '{usuario_original_username}'..."))
        usuario_original.delete()
        self.stdout.write(self.style.SUCCESS(f"¡Usuario '{usuario_original_username}' eliminado exitosamente!"))