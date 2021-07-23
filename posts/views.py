from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import UserPost
from .forms import PostForm

class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = UserPost
    template_name = "post.html"
    context_object_name = 'post'
    

class AddPost(LoginRequiredMixin, CreateView):
    login_url = '/login'
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/'
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self , **kwargs):
        #we get teh contenxt
        #then create a new value
        context = super().get_context_data(**kwargs)
        context['value'] = "Submit" 
        return context

     

        

    
  
