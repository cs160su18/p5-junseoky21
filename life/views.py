from django.shortcuts import render
from django.core import serializers
from life.models import *
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    all_groups = Group.objects.all()
    return render(request, 'life/index.html', {"groups": all_groups})

def view(request):
    all_groups = Group.objects.all()
    return render(request, 'life/view.html', {"groups": all_groups})

def enter(request):
    all_groups = Group.objects.all()
    return render(request, 'life/enter.html', {"groups": all_groups})

def make_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Error")
    all_restaurants = Restaurant.objects.all()
    return render(request, 'life/makereview.html', {"restaurants": all_restaurants})
