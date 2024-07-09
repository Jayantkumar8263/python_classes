from django.db import models

# Create your models here.

class product_details(models.Model):
    product_category = models.ForeignKey("category", on_delete=models.CASCADE)
    product_name= models.CharField(max_length = 50)
    product_price = models.FloatField(max_length = 50)
    product_quality = models.IntegerField(max_length = 50)
    product_description = models.TextField(max_length = 150)
    #images= models.FileField(upload_to=None, max_length=100)
    product_on_sale= models.BooleanField(max_length = 50)
    product_discount = models.FloatField(max_length = 50)
    product_discount_price = models.FloatField(max_length = 50)
    product_discount_percentage = models.FloatField(max_length = 50)
    
    
class category(models.Model):
    product_category = models.CharField( max_length=50)
    
   