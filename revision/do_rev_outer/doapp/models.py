from django.db import models

# Create your models here.

class do_mod(models.Model):
    name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=50)