from django.db import models

# Create your models here.

class product_details(models.Model):
    order_noumber= models.CharField(max_length = 50)
    product_id = models.CharField(max_length = 50)
    product_name = models.CharField(max_length = 50)
    product_description = models.CharField(max_length = 150)
    price = models.CharField(max_length = 50)