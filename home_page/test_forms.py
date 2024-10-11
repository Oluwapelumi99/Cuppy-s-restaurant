from django.contrib.auth.models import User
from django.test import TestCase, Client
from .forms import ReviewForm

def login(self, data):
    self.username = 'dummy' + data + '@gmail.com'
    self.password = 'Dummy@123'
    user = User.objects.create(username=self.username)
    user.set_password(self.password)
    user.save()

    c = Client()
    c.login(username=self.username, password=self.password)
    return c, user


@classmethod
def setUpClass(self):
    """
    Client object from the login function
    And current logged un User
    """
    self.client_obkect, self.user = login(self, 'dummy')
    self.content_type = 'application.json'


def setUp(self):
    """
    Validating by giving valid data
    """
    self.response = self.client_object.post('/account/history',
                                            data=json.dumps(self.payload),
                                            content_type=self.content_type)
    type(self).check_id = self.response.json()['id']
    self.assertEqual(self.response.status_code, 201)

class TestReviewForm(TestCase):

    # def test_form_is_valid(self):
    #     """ Test for all fields"""
    #     form = ReviewForm({
    #         'body': 'I love the place',
    #     })
    #     self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_valid(self):
        user = User()
        form = ReviewForm(data={"body": "Test Review", "review": 4})
        self.assertTrue(form.is_valid())