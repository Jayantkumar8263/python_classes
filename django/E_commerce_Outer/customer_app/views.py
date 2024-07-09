from django.shortcuts import render
from customer.forms import UserRegistration
# Create your views here.
from django.contrib.auth.models import User
def home(request):
    form = UserRegistration()#object creation
    return render (request, '.html', {'form' : form})