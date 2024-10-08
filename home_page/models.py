from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django_google_maps import fields as map_fields


# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField(max_length=1024, blank=True)
    rating = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def average_rating(self) -> float:
        return self.rating.objects.all().aggregate(Avg('rating'))['rating__avg'] or 0
    def __str__(self):
        return f"{self.author} "

class Location(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)


# class Rating(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
#     rating = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.author}: {self.rating}"