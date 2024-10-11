from django.contrib.auth.models import User
from django.test import TestCase
from .forms import ReviewForm



class TestReviewForm(TestCase):
    

    def test_form_is_valid(self):
        form = ReviewForm({"body": "Test Review", 'rating': '4'})
        self.assertTrue(form.is_valid())

    
    def test_form_is_invalid(self):
        review_form = ReviewForm({'body': ''})
        self.assertFalse(review_form.is_valid(), msg="Form is valid")

    
    def rating_required(self):
        review_form = ReviewForm({'body': 'Test form', 'rating': '4'})