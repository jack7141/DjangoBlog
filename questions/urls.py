
from unicodedata import name
from django.urls import path, include

from questions.models import Question
from . import views


app_name = "questions"

urlpatterns = [
    path("", views.ListQuestionAPIView.as_view(), name="list"),
    path("create/", views.CreateQuestionAPIView.as_view(), name="create"),
    path("<str:title>/", views.DetailQuestionAPIView.as_view(), name="detail"),
    path("<str:title>/review/", views.ListCommentAPIView.as_view(), name="list_comment"),
    # author로 수정요망
    # path("<int:pk>/update/", views.UpdateQuestionAPIView.as_view(), name="update"),
    # path("<int:pk>/delete/", views.DeleteQuestionAPIView.as_view(), name="delete"),    
]