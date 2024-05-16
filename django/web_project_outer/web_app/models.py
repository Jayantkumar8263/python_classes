from django.db import models

# Create your models here.
class detales(models.Model):
    name =  models.CharField(max_length=50)
    mobile = models.CharField( max_length=50)
    email = models.CharField( max_length=200)
    adress = models.CharField( max_length=50)