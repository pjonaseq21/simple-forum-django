from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Post


@receiver(post_save,sender=User)
def create_post(sender,instance,created,**kwargs):
    if created:
        Post.objects.create()
post_save.connect(create_post, sender=User)