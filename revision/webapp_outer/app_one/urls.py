from django.urls import path
from app_one.views import home, delete_a, upd_a
urlpatterns = [
    path('', home, name = "home"),
    path('del/<int:id>', delete_a, name= 'delete'),
    path('upd/<int:id>', upd_a, name= 'update'),
]