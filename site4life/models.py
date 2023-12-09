import os
from django.db import models

# Create your models here.

class danceClasse(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="", upload_to="classes")
    description = models.TextField()
    startDate = models.DateField()
    duration = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
            return f"{self.name}"

class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="", upload_to="events")
    date = models.DateField()
    location = models.TextField()
    ticketPrice = models.IntegerField()

    def __str__(self):
            return f"{self.name}"
        
class Ticket(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchaser_name = models.CharField(max_length=255)
    purchaser_email = models.EmailField()
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return f'"{self.event}" ticket purchased by "{self.purchaser_name}"'