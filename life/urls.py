from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter/',views.enter, name='enter'),
    path('restaurants/',views.restaurants, name='restaurants'),
    path('view/',views.view, name='view'),
    path('process/',views.processMyData, name='process'),
]