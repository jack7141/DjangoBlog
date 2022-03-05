
from .serializers import QuestionSerializer # 생성한 serializer import
from reviews.serializers import ReviewSerializer


from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from reviews.models import Reviews
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    DestroyAPIView, 
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Question 
# Create
class CreateQuestionAPIView(CreateAPIView):
    
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
class ListQuestionAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # 검색
    filter_backends = [SearchFilter]
    search_fields = ('title',)

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
    lookup_field = "title"
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class ListCommentAPIView(APIView):
    """
    get:
        Returns the list of comments on a particular post
    """

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, title):
        question = Question.objects.get(title=title)
        comments = Reviews.objects.filter(question=question)
        serializer = ReviewSerializer(comments, many=True)
        return Response(serializer.data, status=200)