from django.shortcuts import render,redirect
#from django.http import HttpResponse
from web_newapps.models import details
# Create your views here.


def home(request):
    data = details.objects.all()
    
    if request.method =="GET":
        name = request.GET.get('name')
        mobile = request.GET.get('mobile')
        email = request.GET.get('email')
        address = request.GET.get('address')

        if name and mobile and email and address:
            details.objects.create(name = name, mobile = mobile, email = email, address = address)
            return redirect('home')
                
            
    return render(request, 'home.html', {'key' : data})