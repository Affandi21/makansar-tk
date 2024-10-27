# favorite/urls.py
from django.urls import path
from . import views

app_name = 'favorite'

urlpatterns = [
    path('overview/', views.favorite_overview, name='favorite_overview'),
    path('add/<int:product_id>/', views.add_favorite, name='add_favorite'),
    path('delete_favorite/<int:product_id>/', views.delete_favorite, name='delete_favorite'),
    path('promote/<int:product_id>/', views.toggle_top_three, name='toggle_top_three'),
    path('toggle-top-three/', views.toggle_top_three, name='toggle_top_three'),
    path('add_comment/<int:product_id>/', views.add_comment, name='add_comment'),
]
