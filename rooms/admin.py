from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                    "price",
                    "bedrooms",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        ("Lost Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "count_amnenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "city",
        "country",
    )

    ordering = ("name", "price")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    """
    search option prefix:

    ^ : starts with
    = : exact
    @ : search
    none : case insensitive wherever search
    """
    search_fields = ("^city", "host__username")

    """
    self = this
    obj = row
    """

    def count_amnenities(self, obj):
        return obj.amenities.count()

    count_amnenities.short_description = "Amenities Count"

    def count_photos(self, obj):
        return obj.photos.count()

    count_amnenities.short_description = "Photos Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):

        """
        # return f"<img src='{obj.file.url}' />"
        # Django protects against injection by default
        # Use django.utils.html.mark_safe to inject html for django admin panel
        """

        return mark_safe(f"<img width='50px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"
