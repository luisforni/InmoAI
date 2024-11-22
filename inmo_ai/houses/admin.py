from django.contrib import admin
from .models import House

# Register your models here.
class HouseAdmin(admin.ModelAdmin):
    list_display = ('longitude', 'latitude', 'housing_median_age', 'total_rooms',
              'total_bedrooms', 'population', 'households', 'median_income',
              'median_house_value', 'ocean_proximity')

admin.site.register(House, HouseAdmin)