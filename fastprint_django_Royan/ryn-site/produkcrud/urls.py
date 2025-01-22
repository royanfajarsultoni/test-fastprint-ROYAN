from django.urls import path
from . import views

urlpatterns = [
    path('', views.produkFormView, name='home'),
    path('prodview/', views.produkFormView, name='prod_url'),
    path('prodshowview/', views.showView, name='showprod_url'),
    path('prod_update/<int:f_id_produk>', views.updateView, name= 'update_prod_url'),
    path('prod_del/<int:f_id_produk>/', views.deleteView, name= 'delete_prod_url'),

    path('statusview/', views.statusFormView, name='status_url'),
    path('showstatusview/', views.showstatusView, name='showstatus_url'),
    path('status_update/<int:f_id_status>', views.updatestatusView, name= 'update_status_url'),
    path('status_del/<int:f_id_status>/', views.deletestatusView, name= 'delete_status_url'),

    path('kategoriview/', views.kategoriFormView, name='kategori_url'),
    path('showkategoriview/', views.showkategoriView, name='showkategori_url'),
    path('kategori_update/<int:f_id_kategori>', views.updatekategoriView, name= 'update_kategori_url'),
    path('kategori_del/<int:f_id_kategori>/', views.deletekategoriView, name= 'delete_kategori_url'),
]