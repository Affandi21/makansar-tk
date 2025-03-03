from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('seller/', views.seller, name='sellerpage'),
    path('add-makanan-ajax', views.add_makanan_ajax, name='add_makanan_ajax'),
    path('edit-product/<int:id>', views.edit_product, name='edit_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('create-flutter/', views.create_product_flutter, name='create_product_flutter'),
    path('delete-product/', views.delete_product_flutter, name='delete_product_flutter'),
    path('update-product/', views.update_product, name='update_product'),
]