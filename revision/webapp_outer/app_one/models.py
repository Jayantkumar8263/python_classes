from django.db import models

# Create your models here.

class note(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)

