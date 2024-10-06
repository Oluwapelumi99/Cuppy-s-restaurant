from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from .models import Review
from allauth.account.views import EmailConfirmation
from django.core.mail import send_mail
from .forms import ReviewForm
from django.contrib.auth.models import User
from django.views import View
# from urllib.parse import urlencode



# Create your views here.
def review_list(request):
    reviews = Review.objects.all().order_by('-created_on')
    template_name = "home_page/reviews.html"
    return render(request, 'reviews.html', {"reviews": reviews},)

def map_view(request):
    return render(request, 'home_page/location.html')

def index(request):
    review_count = Review.objects.all().count()     
    return render(request, 'home_page/index.html', {"review_count": review_count})

# def email_direct(request):
#     email_address = 'bookingscuppysrestaurant@gmail.com'
#     mailto_link = f'mailto:{urlencode ({"to": email_address})}'
#     return render(request, 'home_page/index.html', {'mailto_link': mailto_link})

@login_required
def submit_review(request):
    if request.method == "POST":
        try:
            form = ReviewForm(request.POST)
            user = get_object_or_404(User, username=request.user)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = user
                review.save()
                messages.add_message(request, messages.SUCCESS, 'Review Created!')
                return redirect('home_page')
            else:
                messages.add_message(request, messages.ERROR, 'Error, Please correct form.')
                return render(request, 'home_page/create_review.html', {"form": form})
        except:
            messages.add_message(request, messages.ERROR, 'Error, Something went wrong')
            return redirect('home_page')
    else:
        form = ReviewForm()
        context = {
            'form': form
        }
        return render(request, 'home_page/create_review.html', context)


def edit_review(request, pk):
    """
    view to edit reviews
    """
    queryset = Review.objects.filter(status=True)
    review = get_object_or_404(Review, pk=pk)
    review_form = ReviewForm(data=request.POST or None, instance=review)
    if request.method == "POST":
        print('got form')
        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            #send to home page
            return redirect('home_page')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')
            #send back to edit page to fix form
            return render(request, 'home_page/reviews.html', context)
    else:
        context={
            'form': review_form
        }

def delete_review(request, pk):
    """
    view to delete reviews
    """
    queryset = Review.objects.filter(status=True)
    review = get_object_or_404(Review, pk=pk)
    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
        return redirect('home_page')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own review!')

# class geocoding(View):
#     template_name = 'home_page/location.html'

#     def get(self, request):
#         return render(request, self.template_name, {'map': map})
        