from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.


# class Booking(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=11)
#     number_of_guests = models.IntegerField()
#     booking_dateandtime_start = models.DateTimeField()
#     booking_dateandtime_end = models.DateTimeField()


class Customer(models.Model):
    title = models.CharField(max_length=10, verbose_name=_('Title'), choices=(('miss', _('Miss')),('ms', _('Ms')),('mrs', _('Mrs')),('mr', _('Mr')),),blank=True)
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    # class Meta:
        # ordering = ["created_on"]
    
    def __str__(self):
        return f"Customer {self.forename}"
    

class Table(models.Model):
    seats = models.IntegerField()
    number_of_guests = models.IntegerField()
    # class Meta:
    #     ordering = ["created_on"]



class Booking(models.Model):
    booking_dateandtime_start = models.DateTimeField()
    booking_dateandtime_end = models.DateTimeField()
    special_request = models.TextField(max_length = 1024)
    cancelled = models.BooleanField(default = False)

    # class Meta:
    #     ordering = ["created_on"]

    # def __str__(self):
    #     return f" {self.created_on}"



