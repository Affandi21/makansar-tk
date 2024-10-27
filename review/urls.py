from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('makanan/<int:makanan_id>/reviews/', views.show_reviews, name='show_reviews'),
    path('makanan/<int:makanan_id>/tambah_review/', views.tambah_review, name='tambah_review'),
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/hapus/', views.hapus_review, name='hapus_review'),
]