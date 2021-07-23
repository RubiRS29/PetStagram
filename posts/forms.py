from django.forms import ModelForm


from .models import UserPost


class PostForm(ModelForm):
    
    class Meta:
        model = UserPost
        fields = ("picture", "description" )

    