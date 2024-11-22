from django.urls import path
from .views import HouseListView, HouseDetailView, HouseCreateView, HouseUpdateView, HouseDeleteView

house_patterns = ([
    path('', HouseListView.as_view(), name='houses'),
    path('<int:pk>/', HouseDetailView.as_view(), name='house'),
    path('create/', HouseCreateView.as_view(), name='create'),
    path('update/<int:pk>/', HouseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', HouseDeleteView.as_view(), name='delete'),
], 'houses')
