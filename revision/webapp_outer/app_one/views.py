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

def delete_a(request, id):
    a = note.objects.get(pk = id)
    a.delete()
    return redirect('home')

def upd_a(request, id):
    a = note.objects.get(pk = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name :
            a.name = name
            a.email = email
            a.save()
            return redirect('home')
        
    return render(request, 'update.html', {'key' : a})