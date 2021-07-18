from django.shortcuts import render
from django.views.generic import ListView



from posts.models import UserPost

class IndexListView(ListView):
    model = UserPost
    template_name = "index.html"
    context_object_name = 'posts'
    


