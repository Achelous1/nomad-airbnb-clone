from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # decorator
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    # 장고 어드민 뷰에서 필드셋으로 폼필드를 나눌 수 있다
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom fieldset",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )
