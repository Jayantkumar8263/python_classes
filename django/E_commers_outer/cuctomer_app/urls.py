from django.urls import path
from cuctomer_app.views import home, registration, ulogin, ulogout, profile

urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', ulogin, name='login'),
    path('logout/', ulogout, name = 'logout'),
    path('profile/<int:i>', profile, name='profile'),
]