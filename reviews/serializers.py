# app이름/serializer.py 생성
from turtle import title
from rest_framework import serializers # serializer import
from .models import Reviews

class ReviewSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source="author.username")
    question=serializers.ReadOnlyField(source="question.title")
    class Meta:
        model = Reviews  
        fields = "__all__"


