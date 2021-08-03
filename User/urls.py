from django.urls import path

from .views import ProfileCreateView, ProfileLogin, logout_view, UserProfileListView, create_follower, UpdateProfileView, FollowProfileListView

app_name = 'profile'
urlpatterns = [
    path('sing_up', ProfileCreateView.as_view(), name='sing_up'),
    path('login', ProfileLogin.as_view(), name='login'),
    path('update/<slug:slug>', UpdateProfileView.as_view(), name='update'),
    path('logout', logout_view , name='logout'),
    path('<str:username>/slug=<slug:slug>', FollowProfileListView.as_view() , name='follow_profile'),
    path('user', UserProfileListView.as_view() , name='user'),
    path('add_follow', create_follower , name='add_follow'),
]
