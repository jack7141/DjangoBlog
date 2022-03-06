import imp
from django.test import TestCase, Client
from rest_framework.test import APITestCase
import json
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APIRequestFactory
from . import views
from .models import Question
import questions

client = Client() 

class TestQuestion(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.url = '/questions/'
        self.view = views.DetailQuestionAPIView.as_view()

    @staticmethod
    def test_setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test200000',
            password='test'
        )

    def test_questions_list(self):
        response = client.get('/questions/', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_questions_create(self):
        import datetime
        now = datetime.datetime.now()
        new_questions = Question.objects.create(
            author_id=self.test_setup_user().id,
            title='django-test',
            body='test',
            created=now, 
            updated=now
        )
        self.assertEqual(new_questions.title, 'django-test')


