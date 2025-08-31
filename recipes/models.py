from django.db import models

# Create your models here.
# recipes/models.py
from django.db import models

class Recipe(models.Model):
    CATEGORIES = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('S', 'Snack'),
        ('DR', 'Drink'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    preparation_time = models.IntegerField(help_text="Time in minutes")
    category = models.CharField(max_length=2, choices=CATEGORIES)
    image = models.ImageField(upload_to='recipe_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title