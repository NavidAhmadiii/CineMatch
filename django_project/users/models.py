from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class CustomUser(AbstractBaseUser):
    # add aditional field
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    bio = models.TextField(max_length=250 ,blank=True)
