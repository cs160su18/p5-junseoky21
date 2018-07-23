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

def processMyData(request):
    if request.method == 'POST':
        print(request.body)
        return HttpResponse('')
    else:
        all_groups = Group.objects.all()
        response = serialize('json', all_groups)
        return HttpResponse(response, content_type="application/json")

    render(request, 'life/processMyData.html', {})

def restaurants(request):
    all_restaurants = Restaurant.objects.all()
    restAndRatings = []
    print("jsoiahgfdsuohsfoaisdjfpiesamjofijewaorwoidpmsad")
    for a in all_restaurants:
        rating = 0
        reviews = Review.objects.filter(restaurant=a)
        counter = 0
        for b in reviews:
            rating += b.rating
            counter += 1
        if counter != 0:
            rating /= counter
        restAndRatings.append([a, rating])
    return render(request, 'life/restaurants.html', {"restaurants": restAndRatings})

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

def checkLocation(customerName, restaurantName, tolerance):
    customer = Customer.objects.filter(name=customerName)
    restaurant = Restaurant.objects.filter(name=restaurantName)
    lat = restaurant[0].latitude
    lng = restaurant[0].longitude
    LL = LocationLogs.objects.filter(customer=customer[0])
    for l in LL:
        if pytagorean(lat - l.latitude, lng - l.longitude) < tolerance:
            return True
    return False

def pytagorean(a, b):
    return math.sqrt(a**2 + b**2)
