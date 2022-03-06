
from .serializers import UserSerializer 
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
)
from rest_framework import status
from rest_framework.response import Response
from .models import User 
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class ListUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(CreateAPIView):
    """
    post:
        Create new user. 
        Returns 토큰.
        parameters: [username, password]
    """
    serializer_class = UserSerializer
    def post(self, request):
        user = User.objects.create_user(username=request.data['username'], password=request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key})

class UserLoginAPIView(APIView):
    """
    post:
        Login user(JSON) 
        key: username, password
        {
            "username": "tokentest2",
            "password":"dlqms1004"
        }

        Returns 토큰.
        parameters: [username, password]
    """
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)