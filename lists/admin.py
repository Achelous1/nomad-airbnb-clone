from django.contrib import admin
from . import models


@admin.register(models.List)
class ListsAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    pass
