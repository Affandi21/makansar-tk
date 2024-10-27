# favorite/forms.py

from django import forms

class ToggleTopThreeForm(forms.Form):
    # Menyimpan ID produk yang akan di-toggle
    product_id = forms.IntegerField(widget=forms.HiddenInput())
