"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path
from posts import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers,serializers,viewsets
from profiles.models import Profile
from posts.models import Post
from profiles.views import CheckProfile
from chat.views import chatView
from chat.views import roomView



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','bio','avatar']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title",'text','created_at']


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



router = routers.DefaultRouter()
router.register(r'profile',ProfileViewSet)
router.register(r'post',PostViewSet)


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profile/<int:pk>', views.profile),
    path('profilecheck/<str:pk>/<int:id>', CheckProfile),
    path("post/<str:pk>", views.post, name='post'),
    path('', include('mailer.urls')),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('chat/', include('chat.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

