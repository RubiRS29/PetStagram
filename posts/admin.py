from django.contrib import admin

from .models import UserPost, Like

@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    exclude = ('slug',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

