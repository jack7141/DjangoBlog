
from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    # 질문에 대한 댓글 생성
    path("<int:question_id>/create", views.CreateReviewAPIView.as_view(), name="create"),
    # 질문에 대한 댓글 리스트
    path("<int:question_id>/", views.ListReviewAPIView.as_view(), name="list"),
]