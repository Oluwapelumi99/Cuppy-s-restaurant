from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from .models import Review, Location
from allauth.account.views import EmailConfirmation
from django.core.mail import send_mail
from .forms import ReviewForm
from django.contrib.auth.models import User
from django.views import View
from django.db.models import Avg
import googlemaps
from django.conf import settings
from pprint import pprint
import requests
import json



# Create your views here.
def review_list(request):
    reviews = Review.objects.all().order_by('-created_on')
    template_name = "home_page/reviews.html"
    return render(request, 'reviews.html', {"reviews": reviews},)

def map_view(request):
    location = Location.objects.all()
    GMAPS_CLIENT = googlemaps.Client(key= settings.GOOGLE_MAPS_API_KEY)
    restaurant_address = 'Osmaston Road, DE1 2EH, Derby, UK'
    response = GMAPS_CLIENT.geocode(restaurant_address)[0]
    geometry = response.get('geometry', {})
    place_id = response.get('place_id', {})
    restaurant1 = geometry.get('location', {})
    lat = restaurant1.get('lat', None)
    lng = restaurant1.get('lng', None)
    print('geocode')
    # location.lat = lat
    # location.lng = lng
    # location.place_id = place_id
    # location.save()
    return render(request, 'home_page/location.html',  {'response':response, 'geometry': geometry, 
    'restaurant1': restaurant1, 'lat':lat, 'lng':lng, 'place_id': place_id})


def get_current_user_location(request):
    print('address')
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data['ip'])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    return render(request, 'home_page/location.html', {'location_data': location_data})


def index(request):
    review_count = Review.objects.all().count()     
    return render(request, 'home_page/index.html', {"review_count": review_count})

# def email_direct(request):
#     email_address = 'bookingscuppysrestaurant@gmail.com'
#     mailto_link = f'mailto:{urlencode ({"to": email_address})}'
#     return render(request, 'home_page/index.html', {'mailto_link': mailto_link})

@login_required
def submit_review(request,pk=None):
    if request.method == "POST":
        try:
            review = Review.objects.get(id=rating_id)
            rating = Review.objects.all(Review, username=request.user).first()
            rating_set.create(username=request.user, rating=rating)
            user_rating = rating.rating if rating else 0
            form = ReviewForm(request.POST)
            user = get_object_or_404(User, username=request.user)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = user
                review.save()
                messages.add_message(request, messages.SUCCESS, 'Review Created!')
                return redirect('home_page')
            else:
                messages.add_message(request, messages.ERROR, 'Error, Please correct form.')
                return render(request, 'home_page/create_review.html', {"form": form})
        except:
            messages.add_message(request, messages.ERROR, 'Error, Something went wrong')
            return redirect('home_page')
    else:
        form = ReviewForm()
        context = {
            'form': form
        }
        return render(request, 'home_page/create_review.html', context)


def rate(request, rating_id):
    review = Review.objects.get(id=rating_id)
    Review.rating.objects.all(Review, username=request.user).delete()
    rating_set.create(username=request.user, rating=rating)
    return render(request, 'home_page/create_review.html', context)



def edit_review(request, pk):
    """
    view to edit reviews
    """
    queryset = Review.objects.filter(status=True)
    review = get_object_or_404(Review, pk=pk)
    review_form = ReviewForm(data=request.POST or None, instance=review)
    if request.method == "POST":
        print('got form')
        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            # send to home page
            return redirect('home_page')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')
            #send back to edit page to fix form
            return render(request, 'home_page/reviews.html', context)
    else:
        context={
            'form': review_form
        }
    return render(request, 'home_page/create_review.html', context)

def delete_review(request, pk):
    """
    view to delete reviews
    """
    queryset = Review.objects.filter(status=True)
    review = get_object_or_404(Review, pk=pk)
    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
        return redirect('home_page')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own review!')
        return render(request, 'home_page/reviews.html', context)

# class geocoding(View):
#     template_name = 'home_page/location.html'

#     def get(self, request):
#         return render(request, self.template_name, {'map': map})
        