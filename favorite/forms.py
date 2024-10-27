from django import forms
from .models import Komentar

class ToggleTopThreeForm(forms.Form):
    # Menyimpan ID produk yang akan di-toggle
    product_id = forms.IntegerField(widget=forms.HiddenInput())

class KomentarForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tambahkan komentar Anda...'}),
        }
        labels = {
            'content': '',
        }
