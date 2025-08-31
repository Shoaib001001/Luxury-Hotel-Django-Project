# home/views.py
from django.shortcuts import render
from .models import Room

def home(request):
    rooms = Room.objects.filter(is_available=True)[:3]
    return render(request, 'home/index.html', {'rooms': rooms})

def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'home/rooms.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'home/room_detail.html', {'room': room})