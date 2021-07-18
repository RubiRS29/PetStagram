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
    user = models.ForeignKey(Profile , on_delete=models.CASCADE)
    description = models.TextField()
    picture = models.ImageField( upload_to='picture_post')
    slug = models.SlugField(max_length=100, unique=True , blank=True)
    created_at = models.DateTimeField( auto_now=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.slug

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug())
        super(UserPost, self).save( *args, **kwargs)


    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
