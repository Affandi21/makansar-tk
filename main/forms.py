from django.forms import ModelForm, RadioSelect, Textarea, ValidationError
from main.models import Makanan
from main.models import UserProfile
from django import forms
from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Makanan
from django.contrib.auth.forms import UserCreationForm
from .models import User
import re

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
        label="Password"  
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Confirm Password"  
    )
    tanggal_lahir = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  
        label="Tanggal Lahir"  
    )
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Nama"  
    )
    no_telp = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="No. Telepon" 
    )
    buyer = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
        label="Buyer",
        required=False 
    )
    seller = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
        label="Seller",
        required=False 
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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nama', 'no_telp']

    # Validasi nama
    def clean_nama(self):
        nama = self.cleaned_data.get('nama')

        if not nama:
            raise ValidationError("Nama tidak boleh kosong!")
        
        if not all(x.isalpha() or x.isspace() for x in nama):
            raise ValidationError("Nama hanya boleh berisi huruf dan spasi.")
            
        return nama

    # Validasi nomor telepon
    def clean_no_telp(self):
        no_telp = self.cleaned_data.get('no_telp')

        if not no_telp:
            raise ValidationError("Nomor telepon tidak boleh kosong!")
        
        if not no_telp.isdigit():
            raise ValidationError("Nomor HP harus terdiri dari angka!")

        if len(no_telp) < 10 or len(no_telp) > 15:
            raise ValidationError("Nomor HP harus memiliki panjang antara 10-15 digit!")

        return no_telp

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'jenis_kelamin', 'email', 'alamat']
        widgets = {
            'jenis_kelamin': RadioSelect(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')]),
            'alamat': Textarea(attrs={'rows': 3}),
        }

    def clean_alamat(self):
        alamat = self.cleaned_data.get('alamat')
        if not alamat:
            raise ValidationError("Alamat tidak boleh kosong!")
        return alamat