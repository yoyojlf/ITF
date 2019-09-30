from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    rut = models.CharField(max_length=11,blank=True)
    birthday = models.DateField(auto_now_add=True,blank=True)
    address = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=12,blank=True)
    bio = models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
