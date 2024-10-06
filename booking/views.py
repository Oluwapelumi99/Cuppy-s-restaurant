from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic 
from django.contrib import messages
from django.http import HttpResponse
from .models import Booking, Table, Customer
from django.views.generic import DeleteView
from datetime import datetime, timedelta
from .forms import BookingForm
from urllib.parse import urlencode




# Create your views here



# def customer_bookings(request, customer_id):
#     """
#     View to display a customer's bookings
#     """ 
#     # customer = Customer.objects.get(Customer, pk=pk)
#     # bookings = Booking.objects.filter(customer=request.user).order_by('-created_on')
#     customer = get_object_or_404(Customer, pk=customer_id)
#     booking = get_object_or_404(Booking, customer=customer)
#     return render(request, 'view_booking.html', {'bookings': bookings},)

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
            table = Table.get_object_or_404()
            if table.approved == True:
                print('table available')
            #     Table.save()
            #     print('table saved')
                form.save(commit=False)
                print('form not saved')
                form.user = request.user
                form.save()
                print('form saved')
                messages.add_message(request, messages.SUCCESS, 'Your booking has been completed succesffully!')
                return render(request, 'booking.html', context )
            else:
                Table.approved = False
                print('table')
                messages.add_message(request, messages.ERROR, 'Table is already reserved')
                return render(request, 'booking/booking.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'Error making booking, Please contact the restaurant')

    return render(request, 'booking/booking.html', context)


# def update_booking(request, pk):
#     """
#     view to update bookings
#     """
#     queryset = Booking.objects.filter()
#     booking = get_object_or_404(Booking, pk=pk)
#     booking_form = BookingForm(data=request.POST or None, instance=booking)
#     current_time = datetime.now()
#     if request.method == "POST":
#         print('got form')
#         if booking.start_time < booking.deadline - current_time:
#             if booking_form.is_valid() and booking.author == request.user:
#                 booking = booking_form.save(commit=False)
#                 booking.save()
#                 messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
#                 return redirect('home_page')
#             else:
#                 messages.add_message(request, messages.ERROR, 'Error updating booking!')
#                 return render(request, 'booking/booking.html', context)
#         else:
#             messages.add_message(request, messages.ERROR, 'You can no longer make changes to this booking!')
#             return render(request, 'booking/booking.html', context)
#     else:
#         context={
#             'form': booking_form
#         }

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


       