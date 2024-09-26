from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import Home, Review
from allauth.account.views import EmailConfirmation
from django.core.mail import send_mail

# Create your views here.

def index(request):      
    home_page = Home.objects.all()
    return render(request, 'home_page/index.html', {"home_page": home_page})

def reviews(request):
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset) 
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

def review_edit(request, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Review.objects.filter(status=1)
        post = get_object_or_404(queryset)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.post = post
            review.approved = False
            review.save("_updated_on")
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('review', args=[slug]))

def review_delete(request, review_id):
    """
    view to delete review
    """
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own review!')

    return HttpResponseRedirect(reverse('review', args=[slug]))