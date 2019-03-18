from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.



class UserProfile(models.Model):
    
    user = models.OneToOneField(User,unique=True, on_delete=models.CASCADE, null=True)
    upliner = models.CharField (max_length=50, default='')
    downliner = models.IntegerField(default=0)
    Maelezo = models.CharField (max_length=100, default='')
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
    
    firstgenb = models.IntegerField(default=0)
    secondgenb = models.IntegerField(default=0)
    thirdgenb = models.IntegerField(default=0)
    fouthgenb = models.IntegerField(default=0)
    fifthgenb = models.IntegerField(default=0)
    

    firstgenr = models.IntegerField(default=0)
    secondgenr = models.IntegerField(default=0)
    thirdgenr = models.IntegerField(default=0)
    fouthgenr = models.IntegerField(default=0)
    fifthgenr = models.IntegerField(default=0)
    
    firstmthb = models.IntegerField(default=0)
    secondmthb = models.IntegerField(default=0)
    thirdmthb = models.IntegerField(default=0)
    fouthmthb = models.IntegerField(default=0)
    fifthmthb = models.IntegerField(default=0)
    sixthmthb = models.IntegerField(default=0)
    totalb = models.IntegerField(default=0)

   
    

    firstmthr = models.IntegerField(default=0)
    secondmthr = models.IntegerField(default=0)
    thirdmthr = models.IntegerField(default=0)
    fouthmthr = models.IntegerField(default=0)
    fifthmthr = models.IntegerField(default=0)
    sixthmthr = models.IntegerField(default=0)
    totalr = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    
    
    
    
    
    

def create_profile(sender, **kwargs):
    if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



