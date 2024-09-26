from django.urls import path
from doapp.views import home

urlpatterns = [
    path('', home, name = "home"),
]
