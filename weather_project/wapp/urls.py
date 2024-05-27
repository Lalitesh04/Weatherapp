from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('weather', views.weather, name='weather'),
]
