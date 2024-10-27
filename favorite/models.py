# favorite/models.py
from django.db import models
from account.models import User
from main.models import Makanan  # Ganti dengan model yang sesuai

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    is_top_three = models.BooleanField(default=False)  # New field for top 3 status
    is_favorite = models.BooleanField(default=False)  # New field for favorite status

    class Meta:
        unique_together = ('user', 'product')  # Hindari duplikasi favorit

class Komentar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    product = models.ForeignKey(Makanan, on_delete=models.CASCADE, related_name="product_comments")
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name="favorite_comments", null=True, blank=True)
    content = models.TextField()
    