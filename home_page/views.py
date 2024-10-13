from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
from django.conf import settings
from django.db.models import Avg
from django.core.mail import send_mail
from allauth.account.views import EmailConfirmation
from .models import Review
from .forms import ReviewForm


# Create your views here.
def review_list(request):
    """
    view to display all reviews to site users
    **context**
    ``reviews``
    *template*
    ``reviews.html``
    """
    reviews = Review.objects.all().order_by('-created_on')
    template_name = "home_page/reviews.html"
    return render(request, 'reviews.html', {"reviews": reviews},)


def index(request):
    """
    view to display the total number of reviews on the home page
    """
    review_count = Review.objects.all().count()
    return render(request, 'home_page/index.html', {"review_count":
                                                    review_count})


@login_required
def submit_review(request):
    """
    view for users to submit reviews
    **context**
    ``review``
    ``form``
    related to forms ReviewForm
    *template*
    ``create_review.html``
    """
    if request.method == "POST":
        try:
            form = ReviewForm(request.POST)
            user = get_object_or_404(User, username=request.user)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = user
                review.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Review Created!')
                return render(request, 'home_page/index.html')
            else:
                messages.add_message(
                    request, messages.ERROR, 'Error, Please correct form.')
                return render(
                    request, 'home_page/create_review.html', {"form": form})
        except Exception:
            messages.add_message(
                request, messages.ERROR, 'Error, Something went wrong')
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
    **context**
    ``review``
    related to an instance of review
    ``form``
    related to forms ReviewForm
    *template*
    ``home_page/create_review.html``
    ``home_page/reviews.html``
    """
    queryset = Review.objects.filter(status=True)
    review = get_object_or_404(Review, pk=pk)
    review_form = ReviewForm(data=request.POST or None, instance=review)
    if request.method == "POST":
        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            return redirect('home_page')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating review!')
            return render(request, 'home_page/reviews.html', context)
    else:
        context = {
            'form': review_form
        }
    return render(request, 'home_page/create_review.html', context)


def delete_review(request, pk):
    """
    view to delete reviews
    **context**
    ``review``
    related to an instance of review
    ``form``
    related to forms ReviewForm
    *template*
    ``home_page``
    ``home_page/reviews.html``
    """
    queryset = Review.objects.filter(status=True)
    review = get_object_or_404(Review, pk=pk)
    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
        return redirect('home_page')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own review!')
        return render(request, 'home_page/reviews.html')
