from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



from posts.models import UserPost
from User.models import UserFollowings

class IndexListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    model = UserPost
    template_name = "index.html"
    context_object_name = 'posts'
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['follow']  = UserFollowings.objects.all()
        return context

