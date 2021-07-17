# imports from django 
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView


#Import same app
from .models import Profile
from .forms import ProfileLoginForm

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
    

    
        



    

    




