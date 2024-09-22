from django.urls import path
from app_one.views import home
urlpatterns = [
    path('', home, name = "home"),
    path('del/<int:id>', delete_data, name= 'delete'),
]
