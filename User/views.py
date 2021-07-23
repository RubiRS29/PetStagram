# imports from django 
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


#Import same app
from .models import Profile
from .forms import ProfileLoginForm

# imports broad 
from posts.models import UserPost

# Create your views here.

class ProfileCreateView(FormView):

    template_name = "profile/sing_up.html"
    form_class = ProfileLoginForm
    success_url = reverse_lazy('PetStagram')


    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self ,  **kwargs):
        context = super().get_context_data(**kwargs)

        context['phrase'] = "Sing up to see photos and videos from your friends"
        context['value'] = "Sing Up"
        return context


class ProfileLogin(LoginView):
    
    # form_class = LoginForm
    template_name = 'profile/login.html'

    def get_context_data(self ,  **kwargs):
        context = super().get_context_data(**kwargs)

        context['phrase'] = "Welcome!"
        context['value'] = "Login"
        return context
    

def logout_view(request):
    logout(request)
    return redirect('/login')


class UserProfileListView(LoginRequiredMixin , ListView):
    login_url = '/login'
    context_object_name = 'user_post'
    model = UserPost
    template_name = 'profile/user_profile.html'
    ordering = '-created_at'

    def get_queryset(self):
        user = self.request.user
        qs = self.model.objects.filter(user=user).all()
        return qs

    def get_context_data(self , **kwargs):
        #we get teh contenxt
        #then create a new value
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context






    




