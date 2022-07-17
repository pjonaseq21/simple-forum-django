from django.shortcuts import render
from chat.models import Room
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chatView(request):
    return render(request,'chat.html', {'rooms': Room.objects.all(),})

from django.shortcuts import render

def roomView(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'room.html',{
        'room':chat_room
    })

