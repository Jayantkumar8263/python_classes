from django.shortcuts import render,redirect
#from django.http import HttpResponse
from web_one_new_app.models import details
# Create your views here.


def home(request):
    data = details.objects.all()
    
    if request.method =="GET":
        name = request.GET.get('name')
        mobile = request.GET.get('mobile')
        email = request.GET.get('email')
        address = request.GET.get('Address')

        if name and mobile and email and address:
            details.objects.create(name = name, mobile = mobile, email = email, address = address)
            return redirect('home')
                
            
    return render(request, 'home1.html', {'key' : data})