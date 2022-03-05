import imp
from django.db import models
from core import models as core_model

class Question(core_model.TimeStampedModel):
    author =  models.ForeignKey('users.User', related_name='questions', on_delete=models.CASCADE)
    title = models.TextField()

    def __str__(self):
        return self.title
