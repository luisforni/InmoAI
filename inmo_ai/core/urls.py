from django.urls import path
from .views import HomePageView, HousePricePredictionView, IncomePredictionView, SamplePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('predict-income/', IncomePredictionView.as_view(), name='income_prediction'),
    path('prediccion/', HousePricePredictionView.as_view(), name='house_price_prediction'),
    path('sample/', SamplePageView.as_view(), name="sample"),
]