from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('upload/', views.upload_post, name='upload_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('unlike_post/<int:post_id>/', views.unlike_post, name='unlike_post'),
    path('comment_post/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:post_id>/', views.delete_comment, name='delete_comment'),
]
