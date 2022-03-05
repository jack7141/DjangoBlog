# app이름/serializer.py 생성
from rest_framework import serializers # serializer import
from .models import User # 선언한 모델 import

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = "__all__"