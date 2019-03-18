from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.



class UserProfile(models.Model):
    
    user = models.OneToOneField(User,unique=True, on_delete=models.CASCADE, null=True)
    upliner = models.CharField (max_length=50, default='')
    downliner = models.IntegerField(default=0, null=True)
    Maelezo = models.CharField (max_length=100, default='')
    Proffession = models.CharField (max_length=100, default='')
    country = models.CharField (max_length=100, default='')
    region = models.CharField (max_length=100, default='')
    city = models.CharField (max_length=100, default='')
    #website = models.URLField(default='')
    phone = models.IntegerField(default=0, null=True)
    image = models.ImageField(upload_to='profile_image',null=True, blank=True)
    image2 = models.ImageField(upload_to='profile_image',null=True, blank=True)
    account = models.IntegerField(default=0, null=True)
    debt = models.IntegerField(default=0, null=True)
    accountdescription = models.CharField (max_length=200, default='')
    
    firstgenb = models.IntegerField(default=0, null=True)
    secondgenb = models.IntegerField(default=0, null=True)
    thirdgenb = models.IntegerField(default=0, null=True)
    fouthgenb = models.IntegerField(default=0, null=True)
    fifthgenb = models.IntegerField(default=0, null=True)
    

    firstgenr = models.IntegerField(default=0, null=True)
    secondgenr = models.IntegerField(default=0, null=True)
    thirdgenr = models.IntegerField(default=0, null=True)
    fouthgenr = models.IntegerField(default=0, null=True)
    fifthgenr = models.IntegerField(default=0, null=True)
    
    firstmthb = models.IntegerField(default=0, null=True)
    secondmthb = models.IntegerField(default=0, null=True)
    thirdmthb = models.IntegerField(default=0, null=True)
    fouthmthb = models.IntegerField(default=0, null=True)
    fifthmthb = models.IntegerField(default=0, null=True)
    sixthmthb = models.IntegerField(default=0, null=True)
    totalb = models.IntegerField(default=0, null=True)

   
    

    firstmthr = models.IntegerField(default=0, null=True)
    secondmthr = models.IntegerField(default=0, null=True)
    thirdmthr = models.IntegerField(default=0, null=True)
    fouthmthr = models.IntegerField(default=0, null=True)
    fifthmthr = models.IntegerField(default=0, null=True)
    sixthmthr = models.IntegerField(default=0, null=True)
    totalr = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.user.username
    
    
    
    
    
    
    

def create_profile(sender, **kwargs):
    if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



