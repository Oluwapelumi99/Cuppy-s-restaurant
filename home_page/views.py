from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Home

# Create your views here.

def index(request):      
    home_page = Home.objects.all()
    return render(request, 'home_page/index.html', {"home_page": home_page},)
    
