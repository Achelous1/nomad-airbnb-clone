from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


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
        print(obj.amenities.all())
        return "potata"

    count_amnenities.short_description = "Amenities Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
