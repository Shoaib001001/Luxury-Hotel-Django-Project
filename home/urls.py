# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
]