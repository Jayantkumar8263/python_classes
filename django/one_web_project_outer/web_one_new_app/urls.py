from django.urls import path
from web_one_new_app.views import home

urlpatterns = [
    path('', home, name= 'home'),
]