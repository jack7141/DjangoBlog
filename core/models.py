
from django.db import models

class TimeStampedModel(models.Model):
    '''
    * 모델 생성 관리 모델
    '''
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True