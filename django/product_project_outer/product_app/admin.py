from django.contrib import admin
from product_app.models import product_details

# Register your models here.

class product_details_Admin(admin.ModelAdmin):
    list_display = ['order_noumber', 'product_id', 'product_name', 'product_description', 'price']
    
admin.site.register(product_details, product_details_Admin)