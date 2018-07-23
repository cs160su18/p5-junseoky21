from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter/',views.enter, name='enter'),
    path('restaurants/',views.restaurants, name='restaurants'),
    path('restaurant_reviews/',views.restaurant_reviews, name='restaurant_reviews'),
    path('view/',views.view, name='view'),
    path('process/',views.processMyData, name='process'),
    path('make_review/', views.make_review, name = 'make_review'),
]
