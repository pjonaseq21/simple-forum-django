from django.db import models
from django.contrib.auth.models import User,auth
from django_fields import DefaultStaticImageField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profile_images", default="default.jpg")
    bio = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.user.username

