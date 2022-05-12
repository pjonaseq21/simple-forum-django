from django.shortcuts import render
from .models import Post
from profiles.models import Profile
from django.contrib.auth.models import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts,'profiles':profiles})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html',{'posts': posts})

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def posting(request):
    if request.method == "POST":
        topic = request.POST['topic']
        text = request.POST['text']
        user = Profile.objects.get(user=request.user)
        new_post = Post(title =topic,text =text, profile=user)
        new_post.save()
        return redirect("/")

    
    
    return render(request, 'posting.html')
@login_required
def profile(request,pk):
    profiles = Profile.objects.filter(id=pk)
    return render(request, 'profile.html', {'profiles':profiles})