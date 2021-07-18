from django.urls import path

from .views import PostDetailView 



app_name = 'post'
urlpatterns = [
    path('<str:slug>', PostDetailView.as_view(), name='post'),
]
