from django.urls import path

from .views import ProfileCreateView, ProfileLogin

app_name = 'profile'
urlpatterns = [
    path('sing_up', ProfileCreateView.as_view(), name='sing_up'),
    path('login', ProfileLogin.as_view(), name='login'),
]
