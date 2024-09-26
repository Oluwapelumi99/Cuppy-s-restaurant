from .models import Booking, Table, Customer
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time', 'number_of_guests', 'special_request']
        widgets = {'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}

