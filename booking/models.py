from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.
class Customer(models.Model):
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
    
STATUS = [
    ('1', 'Reserved'),
    ('2', 'Available'),
]
class Table(models.Model):
    seats = models.IntegerField()
    number_of_guests = models.IntegerField()
    status = models.CharField(max_length=20, verbose_name=_('Status')), 
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]


PEOPLE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
]
class Booking(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE, choices=STATUS, default=None, null=True)
    start_time = models.DateTimeField(verbose_name= 'booking_dateandtime_start', null=False, blank=False)
    number_of_guests = models.CharField(choices=PEOPLE_CHOICES, default='2')
    created_on = models.DateTimeField(auto_now_add=True)
    special_request = models.TextField(max_length=1024)
    cancelled = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.table.status = 'reserved' if self.table.bookings.filter(date=self.start_time).exists() else 'available'
        self.table.save()

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f" {self.created_on}"



