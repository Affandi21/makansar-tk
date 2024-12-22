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

    path('discussions-flutter/<int:makanan_id>/', views.list_discussions, name='list_discussions'),
    path('add-discussion-flutter/<int:makanan_id>/', views.add_discussionflutter, name='add_discussionflu'),
    path('update-discussion-flutter/<int:discussion_id>/', views.update_discussionflutter, name='update_discussionflutter'),
    path('delete-discussion-flutter/<int:discussion_id>/', views.delete_discussionflutter, name='delete_discussionflutter'),
    path('add-reply-flutter/<int:discussion_id>/', views.add_replyflutter, name='add_replyflutter'),
    path('update-reply-flutter/<int:reply_id>/', views.update_replyflutter, name='update_replyflutter'),
    path('delete-reply-flutter/<int:reply_id>/', views.delete_replyflutter, name='delete_replyflutter'),
]
