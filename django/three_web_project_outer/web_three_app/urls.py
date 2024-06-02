from django.urls import path
from web_three_app.views import home
urlpatterns = [
    path ('', home, name = 'home')
]