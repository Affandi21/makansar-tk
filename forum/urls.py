from django.urls import path
from .views import show_discussions, add_discussion, update_discussion, delete_discussion, add_reply, update_reply, delete_reply
app_name = 'forum'

urlpatterns = [
    path('discussion/<int:makanan_id>/', show_discussions, name='show_discussions'),
    path('<int:makanan_id>/add/', add_discussion, name='add_discussion'),
    path('discussion/<int:discussion_id>/update/', update_discussion, name='update_discussion'),
    path('discussion/<int:discussion_id>/delete/', delete_discussion, name='delete_discussion'),
    path('discussion/<int:discussion_id>/add_reply/', add_reply, name='add_reply'),
    path('reply/<int:reply_id>/update/', update_reply, name='update_reply'),
    path('reply/<int:reply_id>/delete/', delete_reply, name='delete_reply'),
]
