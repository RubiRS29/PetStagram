import random
import string

from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

class MyUserManager(BaseUserManager):

    def create_user(self , email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.password = self.set_password(password)
        
        user.save(using=self._db)
        
        return user 
   
class Profile(AbstractUser):
    #We need created a User, based on AbstractUser, but with the anothers functions. 
    biography = models.TextField( blank=True, null=True)
    picture = models.ImageField( upload_to='profiles_pictures', blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True , blank=False , null=False)
    follow = models.ManyToManyField("self", verbose_name=("follow"), related_name="follow", blank=True, null=True)
    slug = models.SlugField(
                    max_length=100, 
                    unique=True , 
                    blank=True
                    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.username + slugify(rand_slug()) 
        super(Profile, self).save( *args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('PetStagram')
    

FOLLOW_CHOICES = (
    ('Follow', 'Follow'),
    ('Unfollow', 'Unfollow')
)   

class UserFollowings(models.Model):
    user_id = models.ForeignKey(Profile , related_name='following', on_delete=models.CASCADE)#user log
    following_user_id = models.ForeignKey(Profile , on_delete=models.CASCADE , related_name='followers')#user to follow
    value = models.CharField(choices = FOLLOW_CHOICES , max_length=10 , default='Follow')
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"
