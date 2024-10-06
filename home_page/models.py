from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField(max_length=1024, blank=True)
    rating = models.FloatField(default=None)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.body