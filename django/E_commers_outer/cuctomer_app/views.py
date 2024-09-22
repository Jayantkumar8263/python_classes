from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'home.html')
#for registration
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('login')
    else:
         form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
    
#for login
def ulogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid username or password')
    return render(request, 'login.html')
#for logout
def ulogout(request):
    logout(request)
    return redirect('home')
#for profile
def profile(request, i):
    user = User.objects.get(pk = i)
    return render(request, 'profile.html', {'user' : user})