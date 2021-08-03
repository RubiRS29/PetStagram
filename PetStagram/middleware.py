from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

class CompleteProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user
                if not profile.picture or not profile.biography:
                     if request.path not in [reverse('profile:update', kwargs={'slug': profile.slug}), reverse('profile:logout')]:
                        return HttpResponseRedirect(reverse('profile:update',  kwargs={'slug': profile.slug}))
                        

        response = self.get_response(request)
        return response