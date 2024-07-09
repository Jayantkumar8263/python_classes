from django.urls import path
from product_app.views import home, delete_data, update_data 
urlpatterns = [
    path('', home, name = 'home'),
    path('del/<int:id>', delete_data, name= 'delete'),
    path('update/<int:id>', update_data, name = 'update'),
]