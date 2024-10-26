# favorite/models.py
from django.db import models
from account.models import User
from main.models import Makanan  # Ganti dengan model yang sesuai

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    is_top_three = models.BooleanField(default=False)  # New field for top 3 status

    class Meta:
        unique_together = ('user', 'product')  # Hindari duplikasi favorit
