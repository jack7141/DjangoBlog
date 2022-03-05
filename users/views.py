
from rest_framework import viewsets # vieset import
from .serializers import UserSerializer # 생성한 serializer import
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .models import User 


class ListTodoAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateTodoAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
