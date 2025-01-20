from django.urls import path
from . import views

urlpatterns = [
    path('', views.produkFormView, name='home'),
    path('prodview/', views.produkFormView, name='prod_url'),
    path('prodshowview/', views.showView, name='showprod_url'),
    path('prod_update/<int:f_id_produk>', views.updateView, name= 'update_prod_url'),
    path('prod_del/<int:f_id_produk>', views.deleteView, name= 'delete_prod_url'),
]