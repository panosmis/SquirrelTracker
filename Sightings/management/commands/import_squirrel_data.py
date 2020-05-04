from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'], encoding = 'utf-8') as fp:
            reader = csv.DictReader(fp)
            data = list(reader) 

        for x in data:
            s = Squirrel(
                Y = x['Y'],
                X = x['X'],
                UniqueID = x['Unique Squirrel ID'],

            )
            s.save()
