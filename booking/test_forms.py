from django.contrib.auth.models import User
from django.test import TestCase
from .forms import BookingForm



class TestBookingForm(TestCase):
    

    def test_form_is_valid(self):
        form = BookingForm({'start_time': '2024-10-31T23:16', 'number_of_guests': '2', 'special_request': 'Test Form'})
        self.assertTrue(form.is_valid(), msg='Form is not valid')

    
    def test_form_is_invalid(self):
        booking_form = BookingForm({'start_time': '', 'number_of_guests': '2', 'special_request': 'Test Form'})
        self.assertFalse(booking_form.is_valid(), msg="Form is valid")
