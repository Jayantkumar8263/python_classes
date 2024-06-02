from django.urls import path
from web_newapps.views import home

urlpatterns = [
    path('', home, name = 'home'),
]