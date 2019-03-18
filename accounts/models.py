from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.



class UserProfile(models.Model):
    
    
    upliner = models.CharField (max_length=50, default='')
   
    Maelezo = models.CharField (max_length=100, default='')
    Proffession = models.CharField (max_length=100, default='')
    country = models.CharField (max_length=100, default='')
    region = models.CharField (max_length=100, default='')
    city = models.CharField (max_length=100, default='')
    #website = models.URLField(default='')
  
    image = models.ImageField(upload_to='profile_image',null=True, blank=True)
    image2 = models.ImageField(upload_to='profile_image',null=True, blank=True)
    
    accountdescription = models.CharField (max_length=200, default='')
    
    
    

    
   
    

    

    def __str__(self):
        return self.username
    
    
    
    
    
    
    

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#             user_profile = UserProfile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=User)



