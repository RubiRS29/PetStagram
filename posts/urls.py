from django.urls import path

from .views import PostDetailView, AddPost, like_post



app_name = 'post'
urlpatterns = [
    path('add_post', AddPost.as_view(), name='add_post'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post'),
    path('like_post', like_post, name='like_post')
]
