from django.db import models
from django.contrib.auth.models import AbstractUser
# Atribut yang dicommand jangan diuncommand karena dapat menyebabkan error

# Model untuk implementasi 2 role pengguna
# class CustomUser(AbstractUser):
#     USER_ROLES = (
#         ('seller', 'Seller'),
#         ('buyer', 'Buyer'),
#     )
#     role = models.CharField(max_length=10, choices=USER_ROLES, default='buyer')

# Model untuk penjual
class ProductEntry(models.Model):
    # seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
    #         limit_choices_to={'role': 'seller'})   # Akses ke seller (penjual)
    food_name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    shop_name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    food_desc = models.TextField()
    rating_default = models.DecimalField(decimal_places=1, max_digits=5)    # Memberi rating default
    # Date/time
    date = models.DateField(auto_now_add=True)

# Model untuk pembeli
class ProductOrder(models.Model):
    # buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
    #       limit_choices_to={'role': 'buyer'})
    # product = models.ForeignKey(ProductEntry,       # Akses ke buyer (pembeli)
    #        on_delete=models.CASCADE)                # Menghubungkan dengan produk yang tersedia
    quantity = models.IntegerField(default=1)
    review = models.TextField()
    rating = models.IntegerField(                   # Rating dari buyer (pembeli)
        default=0,
        choices=[(i, str(i)) for i in range(6)]     # rate dari 1 - 5
    )
    # Date/time
    date = models.DateField(auto_now_add=True)


