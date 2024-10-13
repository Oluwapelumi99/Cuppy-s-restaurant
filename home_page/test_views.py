from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm
from .models import Review
from django.urls import reverse


class TestReviewViews(TestCase):

    def setUp(self):
        """ Set up a staff user and log them in
        to test the blog crud functionality
        """
        username="myUsername",
        email="test@test.com",
        password="myPassword"
        user_model = get_user_model()
        self.user = user_model.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        log_in = self.client.login(password=password,
            email=email
            )

        #confirm user is logged in
        self.assertTrue(log_in)
        self.assertTrue(self.user.is_staff)
        # create a review for the database
        # body="Test review views",
        # objecrating="4",
        # self.review = Review.(body="Test review views", author=self.user,
        #                  rating="4",
        #                  )
        # self.review.save()


    def test_render_review_page_with_review_form(self):
        response = self.client.get(reverse(
                'review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test review views", response.content)
        self.assertIn(b"4", response.content)


  
