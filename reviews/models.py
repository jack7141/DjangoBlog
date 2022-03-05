import imp
from django.db import models
from core import models as core_model
from questions.models import Question
from users.models import User

class Reviews(core_model.TimeStampedModel):
    question = models.ForeignKey(Question, related_name='questions',on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    is_like = models.BooleanField(null=True, default=False)

    class Meta:
        ordering = ["-created", "-updated"]