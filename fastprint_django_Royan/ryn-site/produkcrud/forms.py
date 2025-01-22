from django import forms
from .models import produk, status,  kategori

class produkForm(forms.ModelForm):
    class Meta:
        model = produk
        fields = ['nama_produk', 'kategori_id', 'harga', 'status_id']

        labels = {
            'id_produk' : 'ID Produk',
            'nama_produk' : 'Nama Produk' ,
            'kategori_id' : 'Kategori Produk' ,
            'harga' : 'Harga Produk',
            'status_id' : 'Status Produk' ,
        }

        #status_id  = forms.ModelChoiceField(queryset=status.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='Status Produk')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status_id'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['status_id'].queryset = status.objects.all()  # Mengambil data dari tabel status
        self.fields['status_id'].empty_label = "Pilih Status"  # Placeholder untuk dropdown

        self.fields['kategori_id'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['kategori_id'].queryset = kategori.objects.all()  # Mengambil data dari tabel kategori
        self.fields['kategori_id'].empty_label = "Pilih Kategori"  # Placeholder untuk dropdown

        self.fields['nama_produk'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Produk - cth. Laher Mobil'})
        #self.fields['kategori_id'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kategori Produk - cth. Sparepart'})
        self.fields['harga'].widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga Produk - cth. 10000'})


        self.error_messages = {
            'nama_produk' : {
                'required' : 'Nama Produk harus diisi'
            },
            'kategori_id' : {
                'required' : 'Kategori Produk harus diisi'
            },
            'harga' : {
                'required' : 'Harga Produk harus diisi'
            },
            'status_id' : {
                'required' : 'Status Produk harus diisi'
            }
        }

class editprodukForm(forms.ModelForm):
    class Meta:
        model = produk
        fields = ['nama_produk', 'kategori_id', 'harga', 'status_id']

        labels = {
            'id_produk' : 'ID Produk',
            'nama_produk' : 'Nama Produk' ,
            'kategori_id' : 'Kategori Produk' ,
            'harga' : 'Harga Produk',
            'status_id' : 'Status Produk' ,
        }

        #status_id  = forms.ModelChoiceField(queryset=status.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),label='Status Produk')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_produk'] = forms.CharField(
            widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            initial=self.instance.id_produk if self.instance else 'NONE'  # Menambahkan nilai ID produk
        )

        self.fields['status_id'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['status_id'].queryset = status.objects.all()  # Mengambil data dari tabel status
        self.fields['status_id'].empty_label = "Pilih Status"  # Placeholder untuk dropdown

        self.fields['kategori_id'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['kategori_id'].queryset = kategori.objects.all()  # Mengambil data dari tabel kategori
        self.fields['kategori_id'].empty_label = "Pilih Kategori"  # Placeholder untuk dropdown

        self.fields['nama_produk'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Produk - cth. Laher Mobil'})
        #self.fields['kategori_id'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kategori Produk - cth. Sparepart'})
        self.fields['harga'].widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga Produk - cth. 10000'})


        self.error_messages = {
            'nama_produk' : {
                'required' : 'Nama Produk harus diisi'
            },
            'kategori_id' : {
                'required' : 'Kategori Produk harus diisi'
            },
            'harga' : {
                'required' : 'Harga Produk harus diisi'
            },
            'status_id' : {
                'required' : 'Status Produk harus diisi'
            }
        }

class statusForm(forms.ModelForm):
    class Meta:
        model = status
        fields = ['nama_status']
        labels = {
            'nama_status' : 'Nama Status' ,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_status'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Status Baru'})

        self.error_messages = {
            'nama_status' : {
                'required' : 'Nama Status harus diisi'
            },
        }

class editstatusForm(forms.ModelForm):
    class Meta:
        model = status
        fields = ['id_status','nama_status']

        labels = {
            'id_status' : 'ID Status',
            'nama_status' : 'Nama Status' ,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_status'] = forms.CharField(
            widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            initial=self.instance.id_status if self.instance else 'NONE'  # Menambahkan nilai ID produk
        )
        self.fields['nama_status'].widget = forms.TextInput(attrs={'class': 'form-control'})


        self.error_messages = {
            'nama_status' : {
                'required' : 'Nama Status harus diisi'
            },
        }


class kategoriForm(forms.ModelForm):
    class Meta:
        model = kategori
        fields = ['nama_kategori']
        labels = {
            'nama_kategori' : 'Nama Kategori' ,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_kategori'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Kategori Baru'})

        self.error_messages = {
            'nama_kategori' : {
                'required' : 'Nama Kategori harus diisi'
            },
        }

class editkategoriForm(forms.ModelForm):
    class Meta:
        model = kategori
        fields = ['id_kategori','nama_kategori']

        labels = {
            'id_kategori' : 'ID Kategori',
            'nama_kategori' : 'Nama Kategori' ,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_kategori'] = forms.CharField(
            widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            initial=self.instance.id_kategori if self.instance else 'NONE' 
        )
        self.fields['nama_kategori'].widget = forms.TextInput(attrs={'class': 'form-control'})


        self.error_messages = {
            'nama_kategori' : {
                'required' : 'Nama Kategori harus diisi'
            },
        }