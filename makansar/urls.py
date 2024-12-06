from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('account/', include('account.urls')),
    path('favorite/', include(('favorite.urls', 'favorite'), namespace='favorite')),
    path('review/', include('review.urls')),
    path('forum/', include('forum.urls', namespace='forum')),
    path('', include('main.urls')),
]