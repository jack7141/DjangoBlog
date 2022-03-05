import imp
from django.db import models
from core import models as core_model
from questions.models import Question
from users.models import User

class Reviews(core_model.TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    class Meta:
        ordering = ["-created", "-updated"]