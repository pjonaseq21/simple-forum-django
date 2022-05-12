from django.urls import path

from posts.views import logout, posting
from .views import sendMail,login
from profiles.views import register_request

urlpatterns = [
    path('login', login),
    path('logout', logout),
    path('posting', posting),
    path('register', register_request),
]
