from django.db import models

# Create your models here.
# home/models.py
from django.db import models

class Room(models.Model):
    ROOM_TYPES = (
        ('S', 'Standard'),
        ('D', 'Deluxe'),
        ('P', 'Premium'),
    )
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=1, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField()
    amenities = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f"Room {self.room_number} - {self.get_room_type_display()}"

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.room}"