from django.db import models
from account.models import User
from main.models import Makanan

# Create your models here.
class Review(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)