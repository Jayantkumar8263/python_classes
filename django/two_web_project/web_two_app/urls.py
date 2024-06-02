from django.urls import path
from web_two_app.views import home

urlpatterns = [
    path('', home, name= 'home'),
]
