from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    buyer = models.BooleanField('Buyer', default=False)
    seller = models.BooleanField('Seller', default=False)

    nama = models.CharField(max_length=100, blank=True, null=True)  
    no_telp = models.CharField(max_length=15, blank=True, null=True) 
    tanggal_lahir = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.username