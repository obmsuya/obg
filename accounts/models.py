from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullname = models.CharField (max_length=50, default='')
    upliner = models.CharField (max_length=50, default='')
    uplinerphone = models.IntegerField(null=True, blank=True)
    Maelezo = models.TextField()
    Proffession = models.CharField (max_length=100, default='')
    country = models.CharField (max_length=100, default='')
    region = models.CharField (max_length=100, default='')
    city = models.CharField (max_length=100, default='')
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image',null=True, blank=True)
    image2 = models.ImageField(upload_to='profile_image',null=True, blank=True)    
    debt = models.IntegerField(null=True, blank=True)
    
    
    
    def __str__(self):
        return self.user.username

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#            user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#post_save.connect(create_profile, sender=User)



