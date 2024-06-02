from django.urls import path
from trained_app.views import home, delete_data

urlpatterns = [
    path('', home, name = 'home'),
    path('Del/<int:Id>', delete_data, name= 'deleate'),
]
