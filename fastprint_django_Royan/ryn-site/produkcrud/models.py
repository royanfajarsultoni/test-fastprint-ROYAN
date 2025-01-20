from django.db import models

# Create your models here.
class produk(models.Model):

    class Meta:
        db_table = 'produk' 
        managed = False

    id_produk = models.IntegerField(max_length=11, primary_key=True)
    nama_produk = models.CharField(max_length=255)
    kategori_id = models.CharField(max_length=255)
    harga = models.IntegerField(max_length=11)
    status_id = models.CharField(max_length=50)