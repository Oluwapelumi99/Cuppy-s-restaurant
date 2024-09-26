from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Home, Review
from allauth.account.views import EmailConfirmation
from django.core.mail import send_mail
from .forms import ReviewForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):      
    home_page = Home.objects.all()
    return render(request, 'home_page/index.html', {"home_page": home_page})


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

def reviews(request):
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset) 
    reviews = reviews.all().order_by("-created_on")
    reviews_count = reviews.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request)
        if review_form.is_valid():
            review = review_form.save(commit=True)
            review.save()
            messages.add_message(
        request, messages.SUCCESS,
        "Cuppy's has received your review"
    )

    review_form = ReviewForm()


    return render(
        request,
        'home_page/index.html',
        {"reviews": reviews,
        "review_count": review_count,
        "review_form": review_form,
        },
    )

def edit_review(request, pk):
    """
    view to edit reviews
    """
    queryset = Review.objects.filter(status=True)
    review = get_object_or_404(Review, pk=pk)
    review_form = ReviewForm(data=request.POST or None, instance=review)
    if request.method == "POST":
        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            #send to home page
            return redirect('home_page')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')
            #send back to edit page to fix form
            return render(request, 'home_page/edit_review.html', context)
    else:
        context={
            'form': review_form
        }

def delete_review(request, pk):
    """
    view to delete review
    """
    queryset = Review.objects.filter(status=True)
    review = get_object_or_404(Review, pk=pk)
    if review.author == request.user or request.staff:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own review!')

