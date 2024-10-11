from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.
class Customer(models.Model):
    """
    Stores a single customer id  when a booking has been made and assigns the customer to the booking
    """
    title = models.CharField(max_length=10, verbose_name=_('Title'), choices=(('miss', _('Miss')),('ms', _('Ms')),('mrs', _('Mrs')),('mr', _('Mr')),),blank=True)
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Customer {self.forename}"
    

class Table(models.Model):
    """
    Stores a Table object when a booking has been made and assigns the Table to the booking
    """
    seats = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    class Meta:
        ordering = ["created_on"]


PEOPLE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
]
class Booking(models.Model):
    """
    Stores a single booking entry.
    When a booking is deleted, the table and the customer that made the booking is also deleted
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=None, null=True)
    start_time = models.DateTimeField(verbose_name= 'booking_dateandtime_start', null=False, blank=False)
    number_of_guests = models.CharField(max_length=2, choices=PEOPLE_CHOICES, default='2')
    created_on = models.DateTimeField(auto_now_add=True)
    special_request = models.TextField(max_length=1024)
    deadline = models.DateTimeField(default=datetime.now() + timedelta(hours=72))
    draft = models.BooleanField(default=False)
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f" {self.created_on}"



