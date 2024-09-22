from django.shortcuts import render, redirect
from app_one.models import note
# Create your views here.

def home(request):
    a = note.objects.all().order_by ('-id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name:
            note.objects.create(name = name, email = email)
            return redirect('home')
    return render(request, 'home.html', {'key' : a})

def delete_a(request):
    a = note.objects.get(pk = id)
    delete.data()
    return redirect('home')