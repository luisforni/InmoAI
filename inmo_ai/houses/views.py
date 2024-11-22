from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import House
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class HouseListView(ListView):
    model = House
    template_name = 'houses/house_list.html'
    context_object_name = 'house_list'
    paginate_by = 7

class HouseDetailView(DetailView):
    model = House

@method_decorator(login_required, name='dispatch')
class HouseCreateView(CreateView):
    model = House
    fields = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
              'total_bedrooms', 'population', 'households', 'median_income',
              'median_house_value', 'ocean_proximity']

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            house = House.objects.create(**data)
            return JsonResponse({"message": "Inmueble creado exitosamente.", "id": house.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
@method_decorator(login_required, name='dispatch')
class HouseUpdateView(UpdateView):
    model = House
    fields = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
              'total_bedrooms', 'population', 'households', 'median_income',
              'median_house_value', 'ocean_proximity']
    template_name_suffix = '_update_form'

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            house = self.get_object()
            for field, value in data.items():
                if hasattr(house, field):
                    setattr(house, field, value)
            house.save()
            return JsonResponse({
                "message": "Inmueble actualizado exitosamente.",
                "id": house.id
            }, status=200)
        except json.JSONDecodeError:
            return JsonResponse({
                "message": "Error al procesar los datos JSON.",
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "message": f"Error inesperado: {str(e)}",
            }, status=500)

@method_decorator(login_required, name='dispatch')
class HouseDeleteView(DeleteView):
    model = House
    success_url = reverse_lazy('houses:list')
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "Método GET no soportado para eliminación."}, status=405)
    def delete(self, request, *args, **kwargs):
        house = self.get_object()
        house.delete()
        return JsonResponse({"message": "Inmueble eliminado exitosamente."}, status=200)