from django.db import models
from account.models import User 
import uuid

# Class assign data
class Makanan(models.Model):
    category = models.CharField(max_length=20)
    food_name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    shop_name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    rating_default = models.DecimalField(decimal_places=1, max_digits=5)
    food_desc = models.TextField()

# Model untuk dashboard (khusus untuk pembeli nanti)
class UserProfile(models.Model):
    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=10, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')])
    email = models.EmailField()
    nomor_hp = models.CharField(max_length=15)
    alamat = models.TextField()

    def __str__(self):
        return self.nama