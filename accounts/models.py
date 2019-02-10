from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField (max_length=50, default='')
    upliner = models.CharField (max_length=50, default='')
    downliner = models.IntegerField(default=0)
    Maelezo = models.TextField()
    Proffession = models.CharField (max_length=100, default='')
    country = models.CharField (max_length=100, default='')
    region = models.CharField (max_length=100, default='')
    city = models.CharField (max_length=100, default='')
    #website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image',null=True, blank=True)
    image2 = models.ImageField(upload_to='profile_image',null=True, blank=True)
    account = models.IntegerField(default=0)
    debt = models.IntegerField(default=0)
    accountdescription = models.CharField (max_length=200, default='')

    def __str__(self):
        return self.user.username

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#            user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#post_save.connect(create_profile, sender=User)