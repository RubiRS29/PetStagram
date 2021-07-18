from django.contrib import admin

from .models import UserPost

@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    exclude = ('slug',)

