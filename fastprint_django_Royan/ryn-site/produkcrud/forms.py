from django import forms
from .models import produk

class produkForm(forms.ModelForm):
    class Meta:
        model = produk
        fields = '__all__'

        labels = {
            'id_produk' : 'ID Produk',
            'nama_produk' : 'Nama Produk' ,
            'kategori_id' : 'Kategori Produk' ,
            'harga' : 'Harga Produk',
            'status_id' : 'Status Produk' ,
        }

        widgets  ={
            'id_produk' : forms.NumberInput(attrs={'placeholder': 'cth. 101'}),
            'nama_produk' : forms.TextInput(attrs={'placeholder': 'cth. Laher Mobil'}),
            'kategori_id' : forms.TextInput(attrs={'placeholder': 'cth. Sparepart'}),
            'harga' : forms.NumberInput(attrs={'placeholder': 'cth. 10000'}),
            'status_id' : forms.TextInput(attrs={'placeholder': 'cth. aktif'}),

        }