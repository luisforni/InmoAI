from django.core.management.base import BaseCommand
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Entrena y guarda el modelo de predicción del ingreso medio'

    def handle(self, *args, **kwargs):
        # Ruta absoluta del archivo CSV
        csv_path = os.path.join(settings.BASE_DIR, 'houses', 'management', 'commands', 'U4_01_housing.csv')

        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)

            # Variables predictoras y objetivo
            X = df[['population', 'households', 'total_rooms', 'total_bedrooms']]
            y = df['median_income']

            # Dividir en conjunto de entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Entrenar el modelo
            modelo = LinearRegression()
            modelo.fit(X_train, y_train)

            # Guardar el modelo en un archivo .pkl
            model_path = os.path.join(settings.BASE_DIR, 'houses', 'management', 'commands', 'median_income_model.pkl')
            with open(model_path, 'wb') as model_file:
                pickle.dump(modelo, model_file)

            self.stdout.write(self.style.SUCCESS(f'Modelo entrenado y guardado exitosamente en {model_path}'))
        else:
            self.stdout.write(self.style.ERROR(f"El archivo CSV no se encuentra en la ruta {csv_path}"))
