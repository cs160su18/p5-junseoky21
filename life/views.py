from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
    all_groups = Group.objects.all()
    return render(request, 'life/index.html', {"groups": all_groups})