# app이름/serializer.py 생성
from turtle import title
from rest_framework import serializers # serializer import
from .models import Question # 선언한 모델 import

class QuestionSerializer(serializers.ModelSerializer):
    
    # 사용자 이름 = Author 변경
    # id = serializers.CharField()
    author=serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Question  

        fields = (
            'id', 
            'author', 
            'title', 
            'created', 
            'updated'
        )
    
    # def create(self, validated_data):
    #     print(validated_data)
    #     new_questions = Question(
    #         title=validated_data['title'],
    #         Question.objects.get(pk=self.kwargs["pk"])
    #     )
    #     return Question.objects.create(**validated_data)
    '''
    class Meta:
        model = Question  
        fields = "__all__"
    '''


