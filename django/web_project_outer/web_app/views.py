from django.shortcuts import render
from django.http import HttpResponse
from web_app.models import details

# Create your views here.

def home (request):
    return render(request, "home.html")