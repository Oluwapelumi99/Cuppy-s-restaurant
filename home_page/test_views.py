from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm
from .models import Review
from django.urls import reverse

USER_MODEL = get_user_model()


class TestReviewViews(TestCase):

    @classmethod
    def setUpTestData(self):
        self.user = USER_MODEL.objects.create_user(
            email='janedoe@test.com',
            first_name='Jane',
            last_name='Doe',
            username='user123',
            password='password456'
        )

        self.review = Review.objects.create(
            body='My review',
            rating='4',
            author=self.user,
        )

    def test_render_review_page_with_review_form(self):
        response = self.client.get(reverse(
                'review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"review", response.content)
        self.assertIn(b"4", response.content)
