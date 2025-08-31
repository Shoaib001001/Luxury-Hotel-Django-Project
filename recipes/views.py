from django.shortcuts import render

# Create your views here.
# recipes/views.py
from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})