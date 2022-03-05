from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIClient, APIRequestFactory

class TestUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.view = apiviews.PollViewSet.as_view({'post': 'list'})

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            id='testuser@test.com',
            password='test'
        )