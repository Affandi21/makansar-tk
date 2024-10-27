# main/management/commands/import_makanan.py
import json, os
from django.core.management.base import BaseCommand
from main.models import Makanan

class Command(BaseCommand):
    help = 'Import Makanan data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        if not os.path.isabs(json_file):
            json_file = os.path.abspath(json_file)
        if not os.path.exists(json_file):
            self.stdout.write(self.style.ERROR(f'File "{json_file}" does not exist.'))
            return

        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                Makanan.objects.create(
                    category=item['category'],
                    food_name=item['food_name'],
                    location=item['location'],
                    shop_name=item['shop_name'],
                    price=item['price'],
                    rating_default=item['rating_default'],
                    food_desc=item['food_desc']
                )
        self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {json_file}'))