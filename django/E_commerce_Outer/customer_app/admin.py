from django.contrib import admin
from customer_app.models import userdetails

# Register your models here.

class userdetailsadmin(admin.ModelAdmin):
    list_display = [ 'phone', 'address']
    
admin.site.register(userdetails, userdetailsadmin)