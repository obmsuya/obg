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
    
    firstgenb = models.IntegerField(null=True, blank=True)
    secondgenb = models.IntegerField(null=True, blank=True)
    thirdgenb = models.IntegerField(null=True, blank=True)
    fouthgenb = models.IntegerField(null=True, blank=True)
    fifthgenb = models.IntegerField(null=True, blank=True)
    

    firstgenr = models.IntegerField(null=True, blank=True)
    secondgenr = models.IntegerField(null=True, blank=True)
    fouthgenr = models.IntegerField(null=True, blank=True)
    fifthgenr = models.IntegerField(null=True, blank=True)
    
    firstmthb = models.IntegerField(null=True, blank=True)
    secondmthb = models.IntegerField(null=True, blank=True)
    thirdmthb = models.IntegerField(null=True, blank=True)
    fouthmthb = models.IntegerField(null=True, blank=True)
    fifthmthb = models.IntegerField(null=True, blank=True)
    sixthmthb = models.IntegerField(null=True, blank=True)
    totalb = models.IntegerField(null=True, blank=True)

    accountdescription = models.TextField (default='')
    

    firstmthr = models.IntegerField(null=True, blank=True)
    secondmthr = models.IntegerField(null=True, blank=True)
    thirdmthr = models.IntegerField(null=True, blank=True)
    fouthmthr = models.IntegerField(null=True, blank=True)
    fifthmthr = models.IntegerField(null=True, blank=True)
    sixthmthr = models.IntegerField(null=True, blank=True)
    totalr = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#            user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#post_save.connect(create_profile, sender=User)



