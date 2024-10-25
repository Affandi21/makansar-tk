from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.buyer, name='buyerpage'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('seller/', views.seller, name='sellerpage'),
    path('add-makanan-ajax', views.add_makanan_ajax, name='add_makanan_ajax'),
]