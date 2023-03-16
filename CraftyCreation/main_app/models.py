from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
 
# Create your models here.
class Profile(AbstractUser):
    userRole = models.CharField(max_length=30, default = 's'),
    gender = models.CharField(max_length=30, default = 'c'),
    age = models.IntegerField(max_length=30, default = 12),
    category = models.CharField(max_length=60, default = 'F'),
    certification = models.FileField(max_length=60, default ='v')
   


