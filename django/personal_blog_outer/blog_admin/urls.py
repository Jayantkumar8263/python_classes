from django.urls import path
from blog_admin.views import pro_blo
urlpatterns = [
    path('', pro_blo, name='home'),
]
