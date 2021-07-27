from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import UserPost, Like
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



    
def like_post(request):
    user = request.user
    if request.method == 'POST':
        # get from template on the form and  button name
        post_id = request.POST.get('post_id')
        #create an instance of post
        post_obj = UserPost.objects.get(id=post_id)
        #if the user click on unfollow
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
        #if the user click on follow
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
        
    return redirect('PetStagram')

    
  
