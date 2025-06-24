import os
from django.core.management.base import BaseCommand
from django.db.models import Q
from boletines.models import Boletin

class Command(BaseCommand):
    help = 'Updates old media paths for Boletin objects to the new structure.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting path update process...'))
        
        # Busca boletines que todavía usen las rutas viejas
        boletines_to_update = Boletin.objects.filter(
            Q(pdf_file__startswith='boletines_docs/') | Q(photo__startswith='boletines_photos/')
        )

        updated_count = 0
        if not boletines_to_update:
            self.stdout.write(self.style.SUCCESS('No boletines with old paths found. Everything looks correct!'))
            return

        for boletin in boletines_to_update:
            path_changed = False
            
            # Corrige la ruta del PDF
            if boletin.pdf_file and boletin.pdf_file.name.startswith('boletines_docs/'):
                old_path = boletin.pdf_file.name
                new_path = old_path.replace('boletines_docs/', 'boletines/pdfs/', 1)
                boletin.pdf_file.name = new_path
                path_changed = True
                self.stdout.write(f'  PDF path updated for "{boletin.title}": {old_path} -> {new_path}')

            # Corrige la ruta de la foto
            if boletin.photo and boletin.photo.name.startswith('boletines_photos/'):
                old_path = boletin.photo.name
                new_path = old_path.replace('boletines_photos/', 'boletines/portadas/', 1)
                boletin.photo.name = new_path
                path_changed = True
                self.stdout.write(f'  Photo path updated for "{boletin.title}": {old_path} -> {new_path}')
            
            if path_changed:
                boletin.save(update_fields=['pdf_file', 'photo'])
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(f'Process finished. {updated_count} boletines were updated.'))