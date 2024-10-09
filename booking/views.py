from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic 
from django.contrib import messages
from django.http import HttpResponse
from .models import Booking, Table, Customer
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from datetime import datetime, timedelta
from .forms import BookingForm, CancelBookingForm
from urllib.parse import urlencode
from pytz import timezone as tz
from django.contrib.auth.decorators import login_required



# Create your views here


@login_required
def customer_bookings(request):
    """
    View to display a customer's bookings
    """
    bookings = Booking.objects.filter(customer_id=request.user, cancelled=False).order_by('-created_on')
    print(bookings)
    if bookings:
        # bookings.view()
        return render(request, 'view_booking.html', {'bookings': bookings})
    else:
        return redirect('booking') 

def email_direct(request):
    email_address = 'bookingscuppysrestaurant@gmail.com'
    mailto_link = f'mailto:{urlencode ({"to": email_address})}'
    return render(request, 'booking.html', {'mailto_link': mailto_link})


def booking(request):
    """
    view to make bookings
    """
    form = BookingForm(request.POST or None)
    context = {'form': form }
    if request.method == 'POST':
        if form.is_valid():
            print('form valid')
            booking = form.save(commit=False)
            tables = Table.objects.filter(approved=True)
            print(len(tables))
            start_query_time = booking.start_time - timedelta(hours=1, minutes=45)
            end_query_time = booking.start_time + timedelta(hours=2)
            print(start_query_time)
            print(end_query_time)
            available_tables = Table.objects.exclude(booking__start_time__gt=start_query_time, booking__start_time__lt=end_query_time)
            print(available_tables)
            if available_tables.exists():
                booking.table = available_tables.first()
                booking.customer = request.user
                booking.save()
                print('form saved')
                messages.add_message(request, messages.SUCCESS, 'Your booking has been completed succesffully!')
                return render(request, 'booking.html', context )
            else:
               messages.add_message(request, messages.ERROR,'Table already reserved, please pick another time')
               return render(request, 'booking.html', context )
        else:
            messages.add_message(request, messages.ERROR, 'Table is already reserved')
            return render(request, 'booking/booking.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Error making booking, Please contact the restaurant')

    return render(request, 'booking/booking.html', context)


def update_booking(request, pk):
    """
    view to update bookings
    """
    booking = get_object_or_404(Booking, pk=pk)
    booking_form = BookingForm(data=request.POST or None, instance=booking)
    if request.method == "POST":
        current_time = datetime.now()
        print('got form')
        if booking.start_time < booking.deadline.replace(tzinfo=tz('UTC')) - current_time:
            print(booking.deadline)
            if booking_form.is_valid() and booking.author == request.user:
                booking = booking_form.save(commit=False)
                booking.save()
                messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
                return redirect('home_page')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating booking!')
                return render(request, 'booking/booking.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'You can no longer make changes to this booking!')
            return render(request, 'booking/booking.html')
    else:
        context={
            'form': booking_form
        }
    return render(request, 'booking/booking.html', context)


@login_required
def cancel_booking(request, pk):
    """
    view to delete bookings
    """
    booking = get_object_or_404(Booking, id=pk)
    if booking.customer != request.user:
        messages.add_message(request, messages.ERROR, 'You do not have any bookings.')
        return redirect('home_page')
    if request.method == 'POST':
        form = CancelBookingForm(request.POST, instance=booking)
        if form.is_valid():
            cancelled_booking = form.save(commit=False)
            print(cancelled_booking.id)
            print('deleting')
            booking = get_object_or_404(Booking, id=cancelled_booking.id)
            booking.delete()
            return redirect('customer_bookings')
    else:
        form = CancelBookingForm(instance=booking)
        print(form.instance)
        print(booking.id)
        print(form)
        print(form.fields['id'].initial)
        context = {
            'form': form,
            'booking': booking
        }

        return render(request, 'booking/cancel_booking.html', context)
