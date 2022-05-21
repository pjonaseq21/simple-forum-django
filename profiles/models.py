from django.db import models
from django.contrib.auth.models import User,auth
from django.db.models.signals import post_save
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profile_images", default="default.jpg")
    bio = models.CharField(max_length=200,blank=True)
    avatar2 = ImageSpecField(source='avatar',
                                  processors=[ResizeToFill(600, 400)])
    
    
    def __str__(self):
        return self.user.username

def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('profile created!')

post_save.connect(create_profile, sender=User)