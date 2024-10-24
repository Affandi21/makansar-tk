from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('seller/', views.seller, name='sellerpage'),
    path('buyer/', views.buyer, name='buyerpage'),
]