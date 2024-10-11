from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django_google_maps import fields as map_fields
from geopy.geocoders import Nominatim


# Create your models here.

class Review(models.Model):
    """
    Stores a review entry related to model:`auth.User`
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField(max_length=1024, blank=True)
    rating = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]


    def __str__(self):
        return f"{self.author} "



