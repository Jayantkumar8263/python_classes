from django.db import models

from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
# Create your models here.

class userdetails(AbstractUser):
    phone = models.CharField(max_length=50)
    address = models.TextField()
    #image = models.FileField(upload_to=None, max_length=100)
    
    def __str__(self) -> str:
        return self.username
    