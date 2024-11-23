from django.urls import path
from .views import HomePageView, HousePricePredictionView, SamplePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('house_price_prediction/', HousePricePredictionView.as_view(), name='house_price_prediction'),
    path('sample/', SamplePageView.as_view(), name="sample"),
]