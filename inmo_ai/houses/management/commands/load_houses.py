import csv
import os
from django.core.management.base import BaseCommand
from houses.models import House

class Command(BaseCommand):
    help = 'Carga datos de inmuebles desde un archivo CSV.'

    def handle(self, *args, **kwargs):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(base_dir, 'U4_01_housing.csv')

        if not os.path.exists(csv_file_path):
            self.stdout.write(f"El archivo {csv_file_path} no existe.")
            return

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                houses_created = 0

                for row in reader:
                    try:
                        data = {
                            'longitude': float(row['longitude']),
                            'latitude': float(row['latitude']),
                            'housing_median_age': float(row['housing_median_age']),
                            'total_rooms': float(row['total_rooms']),
                            'total_bedrooms': float(row['total_bedrooms']) if row['total_bedrooms'] else 0,
                            'population': float(row['population']),
                            'households': float(row['households']),
                            'median_income': float(row['median_income']),
                            'median_house_value': float(row['median_house_value']),
                            'ocean_proximity': row['ocean_proximity'],
                        }

                        House.objects.create(**data)
                        houses_created += 1

                    except Exception as e:
                        self.stdout.write(f"Error al procesar fila {row}: {e}")

                self.stdout.write(f"Se han cargado {houses_created} inmuebles correctamente.")

        except Exception as e:
            self.stdout.write(f"Error al cargar el archivo: {e}")
