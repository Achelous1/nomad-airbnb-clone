from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversiationAdmin(admin.ModelAdmin):

    """Conversation Admin Definition"""

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Definition"""

    list_display = (
        "message",
        "created",
    )
