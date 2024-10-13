from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm
from .models import Review


class TestReviewViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.review = Review(body="Test review views", author=self.user,
                         rating="4",
                         )
        self.review.save()


    def test_render_review_page_with_review_form(self):
        response = self.client.get(reverse(
                'submit_review'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test review views", response.content)
        self.assertIn(b"4", response.content)
        self.assertIsInstance(
        response.context['form'], ReviewForm)