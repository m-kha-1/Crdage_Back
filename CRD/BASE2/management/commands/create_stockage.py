from django.core.management.base import BaseCommand

from BASE2.models import Stockage



class Command(BaseCommand):
    help = 'Define Stockage'
    
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('media_root', type=str)
        parser.add_argument('media_url', type=str)
        
        
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        media_root = kwargs['media_root']
        media_url = kwargs['media_url']
        
        
        stockage_definition, created = Stockage.objects.get_or_create(
            name=name,
            defaults={'media_root': media_root, 'media_url': media_url}
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Company "{name}" created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Company "{name}" already exists'))