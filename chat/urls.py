from django.urls import path
from . import views


urlpatterns = [
    path('', views.chatView, name='chat-index'),
    path('<str:room_name>/', views.roomView, name='chat_room'),
]
