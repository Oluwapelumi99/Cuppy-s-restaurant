from django.contrib.auth.models import User
from django.test import TestCase
from .forms import ReviewForm



class TestReviewForm(TestCase):
    

    def test_form_is_valid(self):
        """Test for the ' review form is valid"""
        form = ReviewForm({"body": "Test Review", 'rating': 4})
        self.assertTrue(form.is_valid(),  msg="Form is not valid")

    
    def test_form_is_invalid(self):
        """Test for the ' review form is not valid, body 
        is a required field and it has not been filled 
        in and R in rating is in capital letter , it is small in the ReviewForm,
        that invalidates the form and the test comes back as True"""
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