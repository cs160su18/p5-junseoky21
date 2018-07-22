from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter/',views.enter, name='enter'),
    path('view/',views.view, name='view'),
    path('make_review/', views.make_review, name = 'make_review'),
]
