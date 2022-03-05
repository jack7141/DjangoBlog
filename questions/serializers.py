# app이름/serializer.py 생성
from turtle import title
from rest_framework import serializers # serializer import
from .models import Question # 선언한 모델 import

class QuestionSerializer(serializers.ModelSerializer):
    
    author=serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Question  

        fields = (
            'id', 
            'author', 
            'title', 
            'body',
            'total_like',
            'created', 
            'updated'
        )
    


