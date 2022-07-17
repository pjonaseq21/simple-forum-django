from django.urls import path

<<<<<<< HEAD
from posts.views import logout, posting
=======
from posts.views import logout, posting,admininfo
>>>>>>> bd9c3a2f (sss)
from .views import sendMail,login
from profiles.views import register_request

urlpatterns = [
    path('login', login),
    path('logout', logout),
    path('posting', posting),
    path('register', register_request),
<<<<<<< HEAD
=======
    path('admininfo', admininfo),
>>>>>>> bd9c3a2f (sss)
]
