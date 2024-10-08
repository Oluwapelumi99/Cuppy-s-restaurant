from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic 
from django.contrib import messages
from django.http import HttpResponse
from .models import Booking, Table, Customer
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from datetime import datetime, timedelta
from .forms import BookingForm
from urllib.parse import urlencode
from pytz import timezone as tz




# Create your views here



def customer_bookings(request, pk=None):
    """
    View to display a customer's bookings
    """
    bookings = Booking.objects.order_by('-created_on')
    bookings = Booking.objects.filter(customer_id=request.user).order_by('-created_on')
    if Booking.customer==request.user:
        bookings.view()
    return render(request, 'view_booking.html', {'bookings': bookings})

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
                booking.user = request.user
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


def save_draft(self, request):
    form = BookingForm(request.POST or None)
    context = {'form': form }
    if form.cleaned_data.get('draft'):
        form.instance.draft = True
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Booking draft saved succesffully!')
        return render(request, 'booking/booking.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Error saving draft, Please contact the restaurant')
        return render(request, 'booking/booking.html', context)




def update_booking(request, pk):
    """
    view to update bookings
    """
    queryset = Booking.objects.filter()
    booking = get_object_or_404(Booking, pk=pk)
    booking_form = BookingForm(data=request.POST or None, instance=booking)
    current_time = datetime.now()
    if request.method == "POST":
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

# def updateBooking(request, booking_id):

#     """
#     view to update booking
#     """
#     if request.method == "POST":

#         queryset = Booking.objects.filter(status=1)
#         booking = get_object_or_404(booking, pk=booking_id)
#         deadline = booking.start_date - timedelta(hours=72)
#         # comment_form = CommentForm(data=request.POST, instance=comment)

#         if request.post.get('new_booking_dateandtime_start') < deadline and comment.author == request.user:
#             booking = booking.save(commit=False)
#             booking.approved = False
#             booking.save()
#             messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
#         else:
#             messages.info(request, 'Cannot change booking after deadline')
#             return HttpResponseRedirect(reverse('booking_detail', args=[booking_id]))

    # return render(request, 'booking_update.html', {booking:booking})


# class cancel_booking(DeleteView):
#     """
#     view to cancel booking
#     """
#     model = Booking
#     template_name = 'view_booking.html'

#     def post(self, request, pk):
#         booking = self.get_object_or_404(Booking, pk=pk)
#         if booking.author == request.user:
#             booking.cancelled = True
#             booking.save()
#             messages.add_message(request, messages.SUCCESS, 'Booking Canceled!')
#             return redirect('home_page')
#         else:
#             messages.add_message(request, messages.ERROR, 'A problem occured,Please contact the restaurant')


       