from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

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

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'nama', 'no_telp', 'tanggal_lahir', 'buyer', 'seller')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password dan Confirm Password tidak cocok")
        return password2
