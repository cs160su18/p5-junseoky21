from django.shortcuts import render
from django.core import serializers
from life.models import *

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
    # print("jsoiahgfdsuohsfoaisdjfpiesamjofijewaorwoidpmsad")
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

def restaurant_reviews(request):
    reviews = None
    if request.GET.get('name'):
        # message = 'You submitted: %r' % request.GET['q']
        name = str(request.GET.get('name', None))
        print(type(name))
        restaurant = Restaurant.objects.filter(name=name)
        reviews = Review.objects.filter(restaurant=restaurant)
        print(reviews)
    else:
        message = 'No Restaurants Selected!!'
        print (message)
        reviews = ''
    return render(request, 'life/restaurant_reviews.html', {"reviews": reviews})



def enter(request):
    all_groups = Group.objects.all()
    return render(request, 'life/enter.html', {"groups": all_groups})