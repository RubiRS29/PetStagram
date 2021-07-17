from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    exclude = ('password' , 'is_superuser' , )
   
