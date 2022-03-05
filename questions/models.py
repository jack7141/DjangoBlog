import imp
from django.db import models
from core import models as core_model

class Question(core_model.TimeStampedModel):
    author =  models.ForeignKey('users.User', related_name='questions', on_delete=models.CASCADE)
    body = models.TextField()
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    def total_like(self):
        # 좋아요 갯수 카운트
        all_likes = self.questions.all()
        count_like = 0
        for all_like in all_likes:
            if all_like.is_like is True:
                count_like+=1
        return count_like

    class Meta:
        ordering = ["created", "updated"]
