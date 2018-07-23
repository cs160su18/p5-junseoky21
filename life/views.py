from django.shortcuts import render
from django.core import serializers
from life.models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers

jserial = serializers.get_serializer("json")()


def index(request):
    all_groups = Group.objects.all()
    return render(request, 'life/index.html', {"groups": all_groups})

def view(request):
    all_groups = Group.objects.all()
    return render(request, 'life/view.html', {"groups": all_groups})

@csrf_exempt
def users(request):
    all_users = Customer.objects.all()
    print (all_users)
    return render(request, 'life/users.html', {"users" : all_users})

@csrf_exempt
def processMyData(request):
    if request.method == 'POST':
        whatReq = request.POST.get('type', None)
        if whatReq == 'CREATE_USER':
            username = request.POST.get('name')
            print (username)
            newCustomer = Customer(name=username)
            newCustomer.save()
        elif whatReq == 'GET_USERS':
            all_users = Customer.objects.all()
            # jserial.serialize(all_users)
            return HttpResponse(jserial.serialize(all_users))
        elif whatReq == 'CREATE_REVIEW':
            None
        elif whatReq == 'ADD_LOCATION':
            lat = request.POST.get('latitude')
            lng = request.POST.get('longitude')
            name = request.POST.get('name')
            customer = Customer.objects.filter(name=name)[0]
            LocationLog = LocationLogs()
            LocationLog.customer = customer
            LocationLog.latitude = lat
            LocationLog.longitude = lng
            LocationLog.save()
        elif whatReq == 'GET_LOCATIONS':
            name = request.POST.get('name')
            customer = Customer.objects.filter(name=name)[0]
            LocationLog = LocationLogs.objects.filter(customer=customer)
            return HttpResponse(jserial.serialize(LocationLog))
        elif whatReq == 'GET_RESTAURANTS':
            all_restaurant = Restaurant.objects.all()
            return HttpResponse(jserial.serialize(all_restaurant))
        elif whatReq == 'DEL_LOCATIONS':
            name = request.POST.get('name')
            customer = Customer.objects.filter(name=name)[0]
            LocationLogs.objects.filter(customer=customer).delete()
        return HttpResponse('')
    # else:
    #     all_groups = Group.objects.all()
    #     response = serialize('json', all_groups)
    #     return HttpResponse(response, content_type="application/json")

    # render(request, 'life/processMyData.html', {})

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

@csrf_exempt
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
