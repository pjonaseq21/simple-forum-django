from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http.response import HttpResponse
from django import forms
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data["email"]		
			username = form.cleaned_data["username"]
			password1 = form.cleaned_data["password1"]
			password2 = form.cleaned_data["password2"]
			if password1 == password2:
				User.objects.create_user(email=email,username=username,password=password1)
				return redirect("/")
		else:
			print("form failed")
	
	else:
		form = NewUserForm()

	return render (request,'register.html', context={"form":form})
##111