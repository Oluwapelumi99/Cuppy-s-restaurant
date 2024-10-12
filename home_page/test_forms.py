from django.contrib.auth.models import User
from django.test import TestCase
from .forms import ReviewForm



class TestReviewForm(TestCase):
    

    def test_form_is_valid(self):
        form = ReviewForm({"body": "Test Review", 'rating': 4})
        self.assertTrue(form.is_valid(),  msg="Form is not valid")

    
    def test_form_is_invalid(self):
        review_form = ReviewForm({'Rating': '2'})
        self.assertFalse(review_form.is_valid(), msg="Form is valid")


    def test_body_is_required(self):
        """Test for the 'body' field"""
        form = ReviewForm({
            "body": "",
            'rating': '2',
        })
        self.assertTrue(
            form.is_valid(),
            msg="Body was not provided, but the form is valid"
        )


    def test_rating_is_not_required(self):
        """Test for the 'rating' field is not required"""
        form = ReviewForm({
            "body": "Test Review",
            'rating': '',
        })
        self.assertFalse(
            form.is_valid(),
            msg="Rating was not provided, but the form is valid"
        )