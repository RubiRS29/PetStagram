# Native 
import random
import string

#django imports
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# imports from apps
from User.models import Profile
from django.utils.text import slugify


#Create a model for our users add posts
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))


class UserPost(models.Model):
    user        = models.ForeignKey(Profile , on_delete=models.CASCADE)
    description = models.TextField()
    picture     = models.ImageField(upload_to='picture_post')
    liked       = models.ManyToManyField(
                    Profile, 
                    verbose_name=("like"), 
                    related_name="likes"
                    )
    
    slug        = models.SlugField(
                    max_length=100, 
                    unique=True , 
                    blank=True
                    )
    created_at  = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name        = ("Post")
        verbose_name_plural = ("Posts")
        ordering            = ['-created_at']

    def __str__(self):
        return self.slug
    
    def all_likes(self):
        return self.liked.all().count()

    def save(self , *args, **kwargs):
        
        
        if not self.slug:
            self.slug = slugify(rand_slug())
        super(UserPost, self).save( *args, **kwargs)


    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
LIKE_CHOICES = (
    ('Like' , 'like'), 
    ('Unlike' , 'Unlike')
)
class Like(models.Model):
    post    = models.ForeignKey(UserPost , on_delete=models.CASCADE)
    user    = models.ForeignKey(Profile, on_delete=models.CASCADE)
    value   = models.CharField(choices=LIKE_CHOICES, max_length=10 , default='Unlike')
    
    class Meta:
        verbose_name = ("Like")
        verbose_name_plural = ("Likes")

    
