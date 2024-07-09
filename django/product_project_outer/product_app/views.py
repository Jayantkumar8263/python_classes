from django.shortcuts import render, redirect
from product_app.models import product_details
# Create your views here.

def home(request):
    data = product_details.objects.all()
    
    if request.method =="GET":
        order_noumber = request.GET.get('order_noumber')
        product_id = request.GET.get('product_id')
        product_name = request.GET.get('product_name')
        product_description = request.GET.get('product_description')
        price = request.GET.get('price')                                      

        if order_noumber and product_id and product_name and product_description and price :
            product_details.objects.create(order_noumber = order_noumber , product_id = product_id , product_name = product_name, product_description = product_description, price = price)
            return redirect('home')
                
            
    return render(request, 'product.html', {'key' : data})


def delete_data(request , id):
    data = product_details.objects.get(pk = id)
    data.delete()
    return redirect('home')

def update_data(request , id):
    data = product_details.objects.get(pk = id)
    
    if request.method == "GET":
        order_noumber = request.GET.get('order_noumber')
        product_id = request.GET.get('product_id')
        product_name = request.GET.get('product_name')
        product_description = request.GET.get('product_description')
        price = request.GET.get('price')
        if order_noumber and product_id and product_name and product_description and price:
            
            data.order_noumber = order_noumber 
            data.product_id = product_id 
            data.product_name = product_name
            data.product_description = product_description
            data.price = price
            data.save()
            return redirect('home')
    return render(request, 'product1.html', {'key' : data})
    