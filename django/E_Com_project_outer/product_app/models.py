from django.db import models

# Create your models here.

class product_details(models.Model):
    name = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)
    quantity = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250)
    descount_price = models.CharField(max_length = 250)
    descount_percent = models.CharField(max_length = 250)
    on_scale = models.CharField(max_length = 250)
    images = models.CharField(max_length = 250)
    