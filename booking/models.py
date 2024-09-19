from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    number_of_guests = models.IntegerField()
    booking_dateandtime_start = models.DateTimeField()
    booking_dateandtime_end = models.DateTimeField()
    