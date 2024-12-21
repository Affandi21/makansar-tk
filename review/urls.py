from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('makanan/<int:makanan_id>/reviews/', views.show_reviews, name='show_reviews'),
    path('makanan/<int:makanan_id>/tambah_review/', views.tambah_review, name='tambah_review'),
    path('<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('<int:review_id>/hapus/', views.hapus_review, name='hapus_review'),
    path('makanan/<int:makanan_id>/reviews/json/', views.show_json_reviews, name='show_json_reviews'),
    path('makanan/<int:pk>/create-review-flutter/', views.create_review_flutter, name='create_review_flutter'),
    path('current_username/', views.get_current_username, name='get_current_username'),

]