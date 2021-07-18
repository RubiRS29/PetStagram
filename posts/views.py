from django.shortcuts import render
from django.views.generic import DetailView


from .models import UserPost


class PostDetailView(DetailView):
    model = UserPost
    template_name = "post.html"
    context_object_name = 'post'

  




