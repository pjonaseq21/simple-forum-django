from django.urls import path

from posts.views import logout, posting
from .views import sendMail,login


urlpatterns = [
    path('register', sendMail),
    path('login', login),
    path('logout', logout),
    path('posting', posting),
]
