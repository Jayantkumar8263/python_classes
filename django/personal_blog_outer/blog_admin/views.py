from django.shortcuts import render, redirect
from blog_admin.models import Post, Category
# Create your views here.

def pro_blo(request):
    data =  Post.objects.all()
    
    if request.method =="GET":
        title = request.GET.get('title')
        body = request.GET.get('body')
        created_on = request.GET.get('created_on')
        last_modified = request.GET.get('last_modified')
        categories= request.GET.get('categories')
        
        if title and body and created_on and last_modified and categories :
            Post.objects.create(title = title, body = body, created_on = created_on, last_modified = last_modified, categories = categories)
            return redirect('home')
        
    return render(request, 'admin.html', {'key' : data})
    
def cat(request):
    fan = Category.objects.all()
    
    if request.method =="GET":
        name = request.GET.get('name')
        
        if name :
            Category.objects.create(name = name)
            return redirect('home')
        
    return render(request, 'category.html', {'key' : fan})
