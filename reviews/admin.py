from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Reviews)
class QuestionAdmin(admin.ModelAdmin):

    """ Room Admin Definition """
    list_display = (
        "question",
        "author",
        'body'
    )

    list_filter = (
        "question",
        "author",
        "created"
    )
