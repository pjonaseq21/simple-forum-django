from django.core.exceptions import PermissionDenied

# Create your views here.
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
import time
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
				time.sleep(0.5)
				messages.success(request, "Account Created")
				time.sleep(1.5)
		else:
			messages.error(request, "Registration failed, try again")

	else:
		form = NewUserForm()

	return render(request,'register.html', context={"form":form})
##111

@login_required()
def CheckProfile(request, pk, id):
	profiles = Profile.objects.filter(id=id)
	for profile in profiles:
		z = str(profile)
		y = str(request.user)
		if z != y:
			
			print(profile)
			print(request.user)
			raise PermissionDenied
	

		else:
			pass

	return render(request, "editprofile.html",{"profiles": profiles,})