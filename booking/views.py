from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic 
from django.contrib import messages
from django.http import HttpResponse
from .models import Booking, Table, Customer
from django.views.generic import DeleteView
from datetime import timedelta
from .forms import BookingForm


# Create your views here

def booking(request):
    available_tables = Table.objects.filter(seats__gte=1)
    return render(request, 'booking.html', {'available_tables': available_tables})



def makeBooking(request):
    form = BookingForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            table = get
            # here I can check for a table
            form.save(commit=False)
            form.user = request.user
            messages.add_message(request, messages.SUCCESS, 'Your booking has been completed succesffully!')
        else:
            messages.add_message(request, messages.ERROR, 'Error making booking, Please send an email to.........')

        return redirect(reverse('booking'))
        # table_num = int(request.POST['table_num'])
        # date = request.POST['date']
        # time = request.POST['time']
        # people_num = int(request.POST['people_num'])

        # booking = Booking(table_num=table_num, date=date, time=time, people_num=people_num)
        # booking.save(commit=False)
        # booking.post = post 
        # booking.approved = False
        # booking.save()
    #     messages.add_message(request, messages.SUCCESS, 'Your booking has been completed succesffully!')
    # else:
    #     messages.add_message(request, messages.ERROR, 'Error making booking, Please send an email to.........')

    return render(request, 'booking/makebooking.html', context)

    # return HttpResponseRedirect(reverse('booking_detail', args=[slug]))


def updateBooking(request, booking_id):

    """
    view to update booking
    """
    if request.method == "POST":

        queryset = Booking.objects.filter(status=1)
        booking = get_object_or_404(booking, pk=booking_id)
        deadline = booking.start_date - timedelta(hours=72)
        # comment_form = CommentForm(data=request.POST, instance=comment)

        if request.post.get('new_booking_dateandtime_start') < deadline and comment.author == request.user:
            booking = booking.save(commit=False)
            booking.approved = False
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.info(request, 'Cannot change booking after deadline')
            return HttpResponseRedirect(reverse('booking_detail', args=[booking_id]))

    return render(request, 'booking_update.html', {booking:booking})


class cancelBooking(DeleteView):
    model = Booking
    template_name = 'cancel.html'
    success_url = '/'

    def post(self, request, pk):
        booking = self.get_object_or_404()
        booking.cancelled = True
        booking.save()
        return redirect(self.success_url)
