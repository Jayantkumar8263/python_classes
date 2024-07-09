from django.urls import path
from customer_app.views import home

urlpatterns = [
    path('', home, name= 'home'),
]