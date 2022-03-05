from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):

    """ Room Admin Definition """
    list_display = (
        "author",
        "title",
        "body",
        'total_like',
    )

    # list_filter = (
    #     "author",
    # )
