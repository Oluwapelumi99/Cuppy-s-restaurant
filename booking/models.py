from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)

class Table(models.Model):
    size = models.IntegerField()


class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    people = models.IntegerField()
    booking_dateandtime_start = models.DateTimeField()
    booking_dateandtime_end = models.DateTimeField()
    