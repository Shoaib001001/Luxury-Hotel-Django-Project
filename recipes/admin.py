from django.contrib import admin

# Register your models here.
# recipes/admin.py
from django.contrib import admin
from .models import Recipe

admin.site.register(Recipe)