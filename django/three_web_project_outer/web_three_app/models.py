from django.db import models

# Create your models here.

class details(models.Model):
    name = models.CharField(max_length = 50)
    mobile = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 250)