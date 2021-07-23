from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """Custom User Admin"""

    # admin site 리스트에 어떤 항목들을 나타낼지 결정한다
    list_display = ("username", "gender", "language", "currency", "superhost")

    # admin site에서 어떤 필터를 보여줄 지 결정한다
    list_filter = ("language", "superhost")


# 위 코드와 같음
# class CustomUserAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(models.User, CustomUserAdmin)
