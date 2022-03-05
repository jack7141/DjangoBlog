from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """
    list_display = (
        "username",
        "email",
        # 토큰 정보 추가하면 좋을듯
    )