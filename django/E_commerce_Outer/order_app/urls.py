from django.urls import path
from order_app.views import home

urlpatterns = [
    path('', home, name= 'home'), 
]