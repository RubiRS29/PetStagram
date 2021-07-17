#import django 
from django.forms import ModelForm

#import the model
from .models import Profile


class ProfileLoginForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("email", "username" , "password" )
    
    def save(self , commit=True ):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


