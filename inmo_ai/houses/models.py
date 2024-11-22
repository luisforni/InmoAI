from django.db import models

# Create your models here.
class House(models.Model):
    longitude = models.FloatField(help_text="Longitud geográfica del inmueble")
    latitude = models.FloatField(help_text="Latitud geográfica del inmueble")
    housing_median_age = models.FloatField(help_text="Edad promedio de las viviendas en el área")
    total_rooms = models.FloatField(help_text="Número total de habitaciones en el inmueble")
    total_bedrooms = models.FloatField(help_text="Número total de dormitorios en el inmueble")
    population = models.FloatField(help_text="Población en el área")
    households = models.FloatField(help_text="Número de hogares en el área")
    median_income = models.FloatField(help_text="Ingreso medio en el área (en decenas de miles)")
    median_house_value = models.FloatField(help_text="Valor medio del inmueble")
    ocean_proximity = models.CharField(
        max_length=50,
        choices=[
            ('NEAR OCEAN', 'Cerca del océano'),
            ('INLAND', 'Interior'),
            ('NEAR BAY', 'Cerca de la bahía'),
            ('ISLAND', 'Isla'),
            ('<1H OCEAN', 'A menos de 1 hora del océano'),
        ],
        help_text="Proximidad al océano",
    )

    class Meta:
        verbose_name = 'house'
        verbose_name_plural = 'houses'
        ordering = ['population', 'median_house_value']

    def __str__(self):
        return f"Inmueble en ({self.latitude}, {self.longitude}) - ${self.median_house_value}"