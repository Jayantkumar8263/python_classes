from django.urls import path
from product_app.views import home

urlpatterns = [
    path('', home, name= 'home'), 
]