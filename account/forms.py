from django import forms
from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Makanan
from django.contrib.auth.forms import UserCreationForm
from .models import User
import re

class MakananForm(ModelForm):
    CATEGORY_CHOICES = [
        ("Ayam", "Ayam"),
        ("Chinese Food", "Chinese Food"),
        ("Nasi", "Nasi"),
        ("Makanan berkuah", "Makanan berkuah"),
        ("Martabak", "Martabak"),
        ("Arabic Food", "Arabic Food"),
        ("Dessert", "Dessert"),
        ("Daging", "Daging"),
        ("Seafood", "Seafood"),
        ("Beverages", "Beverages"),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Category")

    class Meta:
        model = Makanan
        fields = ["category", "food_name", "location", "price", "food_desc"]

    def clean_food_name(self):
        food_name = self.cleaned_data["food_name"]
        return strip_tags(food_name)

    def clean_location(self):
        location = self.cleaned_data["location"]
        return strip_tags(location)
    
    def clean_shop_name(self):
        shop_name = self.cleaned_data["shop_name"]
        return strip_tags(shop_name)
    
    def clean_food_desc(self):
        food_desc = self.cleaned_data["food_desc"]
        return strip_tags(food_desc)