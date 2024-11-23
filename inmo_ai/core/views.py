from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Avg
from houses.models import House
import pickle
import os
import logging
from django.conf import settings
from django.http import JsonResponse
import json
from django.views import View

logger = logging.getLogger(__name__)

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modelos de AI'

        averages = House.objects.aggregate(
            avg_longitude=Avg('longitude'),
            avg_latitude=Avg('latitude'),
            avg_housing_median_age=Avg('housing_median_age'),
            avg_total_rooms=Avg('total_rooms'),
            avg_total_bedrooms=Avg('total_bedrooms'),
            avg_population=Avg('population'),
            avg_households=Avg('households'),
            avg_median_income=Avg('median_income'),
            avg_median_house_value=Avg('median_house_value')
        )

        context['averages'] = {
            key: str(round(value, 2)).replace(',', '.') if value else '0' 
            for key, value in averages.items()
        }

        return context


class HousePricePredictionView(View):
    def post(self, request, *args, **kwargs):
        print("Cuerpo de la solicitud recibido:", request.body.decode())

        # Ruta del modelo
        model_path = os.path.join(settings.BASE_DIR, 'houses', 'management', 'commands', 'house_price_model.pkl')
        
        try:
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
        except FileNotFoundError:
            return JsonResponse({'message': 'El archivo house_price_model.pkl no se encontró.'}, status=404)

        try:
            # Intenta cargar los datos JSON
            data = json.loads(request.body)
            example_data = [[
                float(data['longitude']),
                float(data['latitude']),
                float(data['housing_median_age']),
                float(data['total_rooms']),
                float(data['total_bedrooms']),
                float(data['population']),
                float(data['households']),
                float(data['median_income'])
            ]]

            # Realizar la predicción
            prediction = model.predict(example_data)[0]
            return JsonResponse({'prediction': round(prediction, 2)})
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Error: El cuerpo de la solicitud no es un JSON válido.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': f'Error al realizar la predicción: {e}'}, status=500)




class SamplePageView(TemplateView):
    template_name = "core/sample.html"
    model = ListView