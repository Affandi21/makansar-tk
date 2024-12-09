from django.urls import path

from forum import views
from .views import *
app_name = 'forum'

urlpatterns = [
    path('discussion/<int:makanan_id>/', show_discussions, name='show_discussions'),
    path('<int:makanan_id>/add/', add_discussion, name='add_discussion'),
    path('discussion/<int:discussion_id>/update/', update_discussion, name='update_discussion'),
    path('discussion/<int:discussion_id>/delete/', delete_discussion, name='delete_discussion'),
    path('discussion/<int:discussion_id>/add_reply/', add_reply, name='add_reply'),
    path('reply/<int:reply_id>/update/', update_reply, name='update_reply'),
    path('reply/<int:reply_id>/delete/', delete_reply, name='delete_reply'),

    path('create-discussion/<int:makanan_id>/', views.create_discussion, name='create_discussion'),
    path('fetch-discussions/<int:makanan_id>/', views.fetch_discussions, name='fetch_discussions'),
    path('edit-discussion/<int:discussion_id>/', views.edit_discussion, name='edit_discussion'),
    path('delete-discussion/<int:discussion_id>/', views.delete_discussion, name='delete_discussion'),
    path('add-reply/<int:discussion_id>/', views.add_reply, name='add_reply'),
    path('edit-reply/<int:reply_id>/', views.edit_reply, name='edit_reply'),
    path('delete-reply/<int:reply_id>/', views.delete_reply, name='delete_reply'),
]
