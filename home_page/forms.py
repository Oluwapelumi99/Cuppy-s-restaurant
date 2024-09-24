from .models import Home, Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ('body',)
