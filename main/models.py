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
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)

# Model untuk dashboard
class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    jenis_kelamin = models.CharField(max_length=10, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')])
    email = models.EmailField()
    alamat = models.TextField()

    def __str__(self):
        return self.user_profile.nama
    
    @property
    def nama(self):
        return self.user_profile.nama

    @property
    def nomor_hp(self):
        return self.user_profile.no_telp