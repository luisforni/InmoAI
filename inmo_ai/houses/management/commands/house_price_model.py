from houses.models import House
from django.core.management.base import BaseCommand
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

class Command(BaseCommand):
    help = 'Entrenar modelo de predicción de median_income'

    def handle(self, *args, **kwargs):
        # Obtener datos de la base de datos
        data = pd.DataFrame(list(House.objects.all().values()))
        
        # Definir variables independientes y dependiente
        X = data[[  # Selecciona todos los campos excepto median_income
            'longitude', 'latitude', 'housing_median_age', 'total_rooms', 
            'total_bedrooms', 'population', 'households', 'median_house_value'
        ]]
        y = data['median_income']  # La variable a predecir

        # Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Entrenar el modelo
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Guardar el modelo
        model_path = os.path.join(os.path.dirname(__file__), 'median_income_model.pkl')
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)

        self.stdout.write(self.style.SUCCESS('Modelo entrenado y guardado en median_income_model.pkl'))
