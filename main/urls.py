from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('show-foods/', views.show_foods, name='show_foods'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('edit-dashboard', views.edit_dashboard, name='edit_dashboard'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('profile/', views.view_profile, name='view_profile'),
    path('show-ayam/', views.show_ayam, name='show_ayam'),
    path('show-daging/', views.show_daging, name='show_daging'),
    path('show-chinese-food/', views.show_chinese_foood, name='show_chinese_food'),
    path('show-arabic-food/', views.show_arabic_food, name='show_arabic_food'),
    path('show-dessert/', views.show_dessert, name='show_dessert'),
    path('show-makanan-berkuah/', views.show_makanan_berkuah, name='show_makanan_berkuah'),
    path('show-seafood/', views.show_seafood, name='show_seafood'),
    path('show-martabak/', views.show_martabak, name='show_martabak'),
    path('show-nasi/', views.show_nasi, name='show_nasi'),
    path('show-beverages/', views.show_beverages, name='show_beverages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)