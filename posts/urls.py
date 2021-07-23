from django.urls import path

from .views import PostDetailView, AddPost



app_name = 'post'
urlpatterns = [
    path('add_post', AddPost.as_view(), name='add_post'),
    path('<str:slug>', PostDetailView.as_view(), name='post'),
]
