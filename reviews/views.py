import imp
from django.shortcuts import get_object_or_404
from reviews.serializers import ReviewSerializer
from rest_framework.generics import (
    CreateAPIView, 
)
from rest_framework.views import APIView
from rest_framework.response import Response
from questions.models import Question
from .models import Reviews
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create Review
class CreateReviewAPIView(CreateAPIView):
    """
    post:
        질문에 대한 댓글 달기 
        - **Request Header:**

        Authorization: {token type] {access token]
        ex) Authorization: Token ee7aed09cc4e2abca4411947767bfee28a550dab
        
        parameters: [author, title, question_id]
    """
    serializer_class = ReviewSerializer

    def post(self, request, question_id, *args, **kwargs):
        question = get_object_or_404(Question, pk=question_id)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, question=question)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)

class ListReviewAPIView(APIView):
    """
    get:
        Returns 선택 질문에 대한 댓글 리턴
    """

    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        comments = Reviews.objects.filter(question=question)
        serializer = ReviewSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

