from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateInForum(ModelForm):
    class Meta:
        model= Post
        fields = "__all__"


