from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from .models import Booking, Table, Customer
from .forms import BookingForm, CancelBookingForm
from urllib.parse import urlencode
from datetime import datetime, timedelta, timezone


# Create your views here


@login_required
def customer_bookings(request):
    """
    View to display a customer's bookings
    ** context **
    ``booking``
    ``customer``
    an instance of booking.customer

    *template*
    ``view_booking.html``
    """
    bookings = Booking.objects.filter(
        customer_id=request.user).order_by('-created_on')
    print(bookings)
    if bookings:
        return render(request, 'view_booking.html', {'bookings': bookings})
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You do not have any bookings.'
            'Please complete the form to make a booking')
        return redirect('booking')


def booking(request):
    """
    view to make bookings
    **context**
    ``booking``
    an instance of booking.customer
    ``tables``
    all approved tables related to table.approved
    ``form``
    related to forms BookingForm
    *template*
    ``booking/booking.html``
    """
    form = BookingForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            booking = form.save(commit=False)
            tables = Table.objects.filter(approved=True)
            start_query_time = booking.start_time - timedelta(
                hours=1, minutes=45)
            end_query_time = booking.start_time + timedelta(hours=2)
            available_tables = Table.objects.exclude(
                booking__start_time__gte=start_query_time,
                booking__start_time__lte=end_query_time)
            if available_tables.exists():
                booking.table = available_tables.first()
                booking.customer = request.user
                booking.save()
                messages.add_message(
                        request, messages.SUCCESS,
                        'Your booking has been completed succesffully!')
                return redirect('home_page')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Table already reserved, please pick another time')
                return render(request, 'booking.html', context)
        else:
            messages.add_message(
                request, messages.ERROR, 'Table is already reserved')
            return render(request, 'booking/booking.html', context)
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Error making booking, Please contact the restaurant')

    return render(request, 'booking/booking.html', context)


def update_booking(request, pk):
    """
    view to update bookings
    **context**
    ``booking``
    an instance of booking.customer
    ``tables``
    all approved tables related to table.approved
    ``form``
    related to forms BookingForm
    *template*
    ``booking/booking.html``
    """
    booking = get_object_or_404(Booking, pk=pk)
    booking_form = BookingForm(data=request.POST or None, instance=booking)
    if request.method == "POST":
        booking = get_object_or_404(Booking, pk=pk)
        if booking_form.is_valid() and booking.customer == request.user:
            booking = booking_form.save(commit=False)
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
            return redirect('home_page')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating booking!')
            return render(request, 'booking/booking.html', context)
    else:
        context = {
            'form': booking_form
        }
    return render(request, 'booking/booking.html', context)


@login_required
def cancel_booking(request, pk):
    """
    view to cancel bookings
    **context**
    ``booking``
    an instance of booking
    ``form``
    related to forms BookingForm
    *template*
    ``booking/cancel_booking.html``
    """
    booking = get_object_or_404(Booking, id=pk)
    if booking.customer != request.user:
        messages.add_message(
            request, messages.ERROR, 'You do not have any bookings.')
        return redirect('home_page')
    if request.method == 'POST':
        form = CancelBookingForm(request.POST, instance=booking)
        if form.is_valid():
            cancelled_booking = form.save(commit=False)
            booking = get_object_or_404(Booking, id=cancelled_booking.id)
            booking.delete()
            messages.add_message(
                request, messages.SUCCESS, 'Booking cancelled')
            return redirect('customer_bookings')
    else:
        form = CancelBookingForm(instance=booking)
        context = {
            'form': form,
            'booking': booking
        }

        return render(request, 'booking/cancel_booking.html', context)
