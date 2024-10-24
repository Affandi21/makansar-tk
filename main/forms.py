from django.forms import ModelForm, RadioSelect, Textarea, ValidationError
from main.models import Makanan
from main.models import UserProfile

class ProductEntryForm(ModelForm):
    class Meta:
        model = Makanan
        fields = ["category", "food_name", "price", "shop_name", "location", "food_desc", "rating_default"]

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nama', 'jenis_kelamin', 'email', 'nomor_hp', 'alamat']
        widgets = {
            'jenis_kelamin': RadioSelect(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')]),
            'alamat': Textarea(attrs={'rows': 3}),
        }
    
    # Validasi Nomor HP
    def clean_nomor_hp(self):
        nomor_hp = self.cleaned_data['nomor_hp']
        
        if not nomor_hp.isdigit():
            raise ValidationError("Nomor HP harus terdiri dari angka!")

        if len(nomor_hp) < 10 or len(nomor_hp) > 15:
            raise ValidationError("Nomor HP harus memiliki panjang antara 10-15 digit!")
        
        return nomor_hp

