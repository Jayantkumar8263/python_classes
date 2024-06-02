from django.contrib import admin
from trained_app.models import details

# Register your models here.

class detailsadmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'address']
    
admin.site.register(details, detailsadmin)