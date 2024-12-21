# favorite/urls.py
from django.urls import path
from . import views

app_name = 'favorite'

urlpatterns = [
    path('overview/', views.favorite_overview, name='favorite_overview'),
    path('add/<int:product_id>/', views.add_favorite, name='add_favorite'),
    path('delete_favorite/<int:product_id>/', views.delete_favorite, name='delete_favorite'),
    path('promote/<int:product_id>/', views.toggle_top_three, name='toggle_top_three'),
    path('toggle-favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('toggle-top-three/<int:product_id>/', views.toggle_top_three_json, name='toggle_top_three_json'),
    path('overview/json/', views.show_json_all_favorites, name='show_json_all_favorites'),
    path('update-note/<int:product_id>/', views.update_note, name='update_note'),
]
