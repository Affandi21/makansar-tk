from django import forms
from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Makanan
from django.contrib.auth.forms import UserCreationForm
from .models import User
import re

class MakananForm(ModelForm):
    class Meta:
        model = Makanan
        fields = ["category", "food_name", "location", "shop_name", "price",
                "rating_default", "food_desc"]

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

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Password"  # Menambahkan label untuk password1
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Confirm Password"  # Menambahkan label untuk password2
    )
    tanggal_lahir = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # HTML5 DateInput widget
        label="Tanggal Lahir"  # Menambahkan label untuk tanggal_lahir
    )
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Nama"  # Menambahkan label untuk nama
    )
    no_telp = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="No. Telepon"  # Menambahkan label untuk no_telp
    )
    buyer = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
        label="Buyer",
        required=False  # Tidak wajib, karena akan divalidasi secara manual
    )
    seller = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
        label="Seller",
        required=False  # Tidak wajib, karena akan divalidasi secara manual
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'nama', 'no_telp', 'tanggal_lahir', 'buyer', 'seller')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password dan Confirm Password tidak cocok")
        return password2
    
    def clean_no_telp(self):
        no_telp = self.cleaned_data.get('no_telp')
        if not no_telp.isdigit():
            raise forms.ValidationError("No. Telepon harus berupa angka.")
        return no_telp

    def clean_nama(self):
        nama = self.cleaned_data.get('nama')
        if not re.match(r'^[a-zA-Z\s]+$', nama):
            raise forms.ValidationError("Nama hanya boleh berisi huruf dan spasi.")
        return nama

    def clean(self):
        cleaned_data = super().clean()
        buyer = self.cleaned_data.get('buyer')
        seller = self.cleaned_data.get('seller')

        if buyer and seller:
            raise forms.ValidationError("Hanya boleh memilih satu antara Buyer atau Seller.")
        elif not buyer and not seller:
            raise forms.ValidationError("Harap pilih salah satu: Buyer atau Seller.")

        return cleaned_data