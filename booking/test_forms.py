from django.contrib.auth.models import User
from django.test import TestCase
from .forms import BookingForm



class TestBookingForm(TestCase):
    

    def test_form_is_valid(self):
        """Test for the 'form is valid"""
        form = BookingForm({'start_time': '2024-10-31T23:16', 'number_of_guests': '2', 'special_request': 'Test Form'})
        self.assertTrue(form.is_valid(), msg='Form is not valid')

    
    def test_form_is_invalid(self):
        """Test for the 'form is not valid, start_time is a required field and an empty string has been passed,
        that invalidates the form and the test comes back as True"""
        booking_form = BookingForm({'start_time': '', 'number_of_guests': '2', 'special_request': 'Test Form'})
        self.assertFalse(booking_form.is_valid(), msg="Form is valid")


    def test_start_time_is_required(self):
        """Test for the 'start_time' field"""
        form = BookingForm({
            'start_time': '',
            'number_of_guests': '2',
            'special_request': 'Test Form'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Start_time was not provided, but the form is valid"
        )


    def test_number_of_guests_is_required(self):
        """Test for the 'number_of_guests' field"""
        form = BookingForm({
            'start_time': '2024-10-31T23:16',
            'number_of_guests': '',
            'special_request': 'Test Form'
        })
        self.assertFalse(
            form.is_valid(),
            msg="number_of_guests was not provided, but the form is valid"
        )


    def test_special_request_is_not_required(self):
        """Test for the 'special_request' field is not required"""
        form = BookingForm({
            'start_time': '2024-10-31T23:16',
            'number_of_guests': '2',
            'special_request': ''
        })
        self.assertTrue(
            form.is_valid(),
            msg="special_request was not provided, but the form is valid"
        )