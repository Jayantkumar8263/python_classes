from django.db import models

# Create your models here.
class order_details(models.Model):
    order_number= models.CharField(max_length = 50)
    user_id = models.CharField(max_length = 50)
    products = models.CharField(max_length = 50)
    order_date = models.CharField(max_length = 150)
    order_time= models.FileField(upload_to=None, max_length=100)
    total_prize= models.CharField(max_length = 50)
    payment_type = models.CharField(max_length = 50)
    shipping_address = models.CharField(max_length = 50)
    order_status = models.CharField(max_length = 50)