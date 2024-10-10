from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["food_name", "price", "shop_name", "location", "food_desc", "rating_default"]

