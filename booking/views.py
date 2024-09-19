from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from .models import Booking

# Create your views here
def booking(request):
    return HttpResponse('This is the booking page')

# def ViewBookingTimes(request, date):
#     available_tables = Table.objects.filter(seats__gte=1)
#     return render(request, 'booking.html', {'available_tables': available_tables})

# def MakeBooking(request):
#     if request.method == 'POST':
#         table_num = int(request.POST['table_num'])
#         date = request.POST['date']
#         time = request.POST['time']
#         people_num = int(request.POST['people_num'])

#         booking = Booking(table_num=table_num, date=date, time=time, people_num=people_num)
#         # booking.save(commit=False)
#         # booking.post = post 
#         # booking.approved = False
#         booking.save()
#         messages.add_message(request, messages.SUCCESS, 'Your booking has been completed succesffully!')
#     else:
#         messages.add_message(request, messages.ERROR, 'Error making booking, Please send an email to.........')

#     return HttpResponseRedirect(reverse('booking_detail', args=[slug]))