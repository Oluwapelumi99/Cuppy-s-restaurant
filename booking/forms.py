from django import forms
from .models import Booking, Table, Customer



# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'


# class TableForm(forms.ModelForm):
#     class Meta:
#         model = Table
#         fields = ['seats']


class BookingForm(forms.ModelForm):
    """
    Provide a form to customers on the booking page to make their bookings
    """
    class Meta:
        model = Booking
        fields = ['start_time', 'number_of_guests', 'special_request']
        widgets = {'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}

    def clean_deadline(self):
        deadline = self.instance.deadline
        if self.instance.start_time < deadline:
            raise forms.ValidationError("Changes cannot be made 3 days to event.")


class CancelBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = []

    def __init__(self, *args, **kwargs):
        super(CancelBookingForm, self).__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(widget=forms.HiddenInput())
        if self.instance and self.instance.pk:
            self.fields['id'].initial = self.instance.pk

