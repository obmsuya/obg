from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.



class UserProfile(models.Model):
    
    user = models.OneToOneField(User,unique=True, on_delete=models.CASCADE, null=True)
    upliner = models.CharField (max_length=50, default='')
    downliner = models.IntegerField(null=True)
    Maelezo = models.CharField (max_length=100, default='')
    Proffession = models.CharField (max_length=100, default='')
    country = models.CharField (max_length=100, default='')
    region = models.CharField (max_length=100, default='')
    city = models.CharField (max_length=100, default='')
    #website = models.URLField(default='')
    phone = models.IntegerField( null=True)
    image = models.ImageField(upload_to='profile_image',null=True, blank=True)
    image2 = models.ImageField(upload_to='profile_image',null=True, blank=True)
    account = models.IntegerField(null=True)
    debt = models.IntegerField(null=True)
    accountdescription = models.CharField (max_length=200, default='')
    
    firstgenb = models.IntegerField(null=True)
    secondgenb = models.IntegerField(null=True)
    thirdgenb = models.IntegerField(null=True)
    fouthgenb = models.IntegerField(null=True)
    fifthgenb = models.IntegerField(null=True)
    

    firstgenr = models.IntegerField(null=True)
    secondgenr = models.IntegerField(null=True)
    thirdgenr = models.IntegerField(null=True)
    fouthgenr = models.IntegerField(null=True)
    fifthgenr = models.IntegerField(null=True)
    
    firstmthb = models.IntegerField(null=True)
    secondmthb = models.IntegerField(null=True)
    thirdmthb = models.IntegerField(null=True)
    fouthmthb = models.IntegerField(null=True)
    fifthmthb = models.IntegerField(null=True)
    sixthmthb = models.IntegerField(null=True)
    totalb = models.IntegerField(null=True)

   
    

    firstmthr = models.IntegerField(null=True)
    secondmthr = models.IntegerField(null=True)
    thirdmthr = models.IntegerField(null=True)
    fouthmthr = models.IntegerField(null=True)
    fifthmthr = models.IntegerField(null=True)
    sixthmthr = models.IntegerField(null=True)
    totalr = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
    
    
    
    
    
    
    

def create_profile(sender, **kwargs):
    if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



