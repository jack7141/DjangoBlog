from django.contrib.auth import get_user_model


from rest_framework.test import APITestCase
from rest_framework.test import APIClient, APIRequestFactory

from . import views

class TestUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.url = '/users/'
        self.user = self.setup_user()
        self.view = views.ListUserAPIView.as_view()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            password='test'
        )

    def test_list(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_list2(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

