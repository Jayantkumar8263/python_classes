from django.shortcuts import render, redirect
from doapp.models import do_mod

# Create your views here.

def home(request):
    a = do_mod.objects.all().order_by ('-id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        if name:
            do_mod.objects.create(name = name, email = email, mobile = mobile, address = address)
            return redirect('home')
    return render(request, 'home.html', {'key' : a})