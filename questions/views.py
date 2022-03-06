
from django.shortcuts import get_object_or_404
from turtle import title
from .serializers import QuestionSerializer # 생성한 serializer import

from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveUpdateDestroyAPIView
)

from .models import Question 

# Create Questions
class CreateQuestionAPIView(CreateAPIView):
    """
    post:
        [헤더에 토큰이 있어야지만 질문을 생성할 수 있습니다.]
        질문 생성 
        - **Request Header:**

        Authorization: {token type] {access token]
        ex) Authorization: Token ee7aed09cc4e2abca4411947767bfee28a550dab
        
        parameters: [title, body]
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Read

@swagger_auto_schema(request_body=QuestionSerializer, manual_parameters=[openapi.Parameter('header_test', openapi.IN_HEADER, description="a header for  test", type=openapi.TYPE_STRING)])
class ListQuestionAPIView(ListAPIView):
    """
    get:
        Returns: Questions의 전체
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # 검색
    # title, body 내부에서 포함된 키워드 모두 검색
    filter_backends = [SearchFilter]
    search_fields = ('title','body',)

        

class DetailQuestionAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns: Questions 디테일. 검색조건: Question 모델의 Title
    put:
        Updates an 현재 타이틀. Returns 변경된 요청 사항 업로드
        parameters: [author, title, pk]
    delete:
        현재 질문 삭제
        parameters = [title, pk]
    """

    queryset = Question.objects.all()
    lookup_field = "pk"
    serializer_class = QuestionSerializer


class ListQuestionRankAPIView(APIView):
    """
    get:
        Returns 월별 베스트 질문 
    """

    def get(self, request, yyyy, mm):
        from datetime import date

        # 년 월 인자로 input
        # 입력한 날짜 질문들 모두 get
        quesions_this_month = Question.objects.filter(created__year=int(yyyy),created__month=int(mm))

        try:
            # 최대 좋아요 갯수 추출
            top_rank_list = max([quesions_this_month[index].total_like() for index in range(len(quesions_this_month))])
            top_rank_questions_list = []
            
            # Question Object내에서 최대 좋아요를 가지고 있는 ID 검출
            for index in range(len(quesions_this_month)):
                if quesions_this_month[index].total_like() == top_rank_list:
                    top_rank_questions_list.append(quesions_this_month[index])
                    
            quesions_this_month = Question.objects.filter(title__in=top_rank_questions_list)

            serializer = QuestionSerializer(quesions_this_month, many=True)
            return Response(serializer.data, status=200)
        except:
            return Response({"result": "There is no result"}, status=status.HTTP_200_OK)
