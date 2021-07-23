from django.urls import path

from .views import ProfileCreateView, ProfileLogin, logout_view, UserProfileListView

app_name = 'profile'
urlpatterns = [
    path('sing_up', ProfileCreateView.as_view(), name='sing_up'),
    path('login', ProfileLogin.as_view(), name='login'),
    path('logout', logout_view , name='logout'),
    path('user', UserProfileListView.as_view() , name='user'),
]
