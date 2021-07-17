from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

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
    biography = models.TextField()
    picture = models.ImageField( upload_to='img/profiles_pictures')
    email = models.EmailField(max_length=254, unique=True , blank=False , null=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username 

    

    
