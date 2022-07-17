from cgitb import text
import profile
from turtle import title
from django.db import models
from django.db.models.fields import DateField, DateTimeField
from datetime import datetime
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile
# Create your models here.


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    gay_or_nah = models.BooleanField(default=True)

@receiver(post_save,sender=Profile)
def create_post(sender,instance,created,**kwargs):
    if created:
        Post.objects.create(profile = instance, title="hehehe",text="to jest test v2")

