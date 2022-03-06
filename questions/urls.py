
from unicodedata import name
from django.urls import path, include

from questions.models import Question
from . import views


app_name = "questions"

urlpatterns = [
    # 질문 리스트
    path("", views.ListQuestionAPIView.as_view(), name="list"),
    # 질문 생성
    path("create/", views.CreateQuestionAPIView.as_view(), name="create"),
    # 질문 수정, 삭제, 디테일
    path("<int:pk>/", views.DetailQuestionAPIView.as_view(), name="detail"),
    # 날짜 별 랭킹
    path("<str:yyyy>/<str:mm>", views.ListQuestionRankAPIView.as_view(), name="ranking"),
]