from django.db import models

# Create your models here.
class produk(models.Model):
    class Meta:
        db_table = 'produk' 
        managed = False

    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=255)
    kategori_id = models.CharField(max_length=255)
    harga = models.IntegerField()
    status_id = models.ForeignKey(
        'status',  # Model yang dijadikan relasi
        on_delete=models.CASCADE,
        db_column='status_id',  # Nama kolom di tabel database
    )


class kategori(models.Model):

    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'kategori' 
        managed = False

    

class status(models.Model):
    def __str__(self):
        return self.nama_status
    
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'status' 
        managed = False

    
    