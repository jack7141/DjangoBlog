# app이름/serializer.py 생성
from turtle import title
from rest_framework import serializers # serializer import
from .models import Reviews

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews  
        fields = "__all__"


