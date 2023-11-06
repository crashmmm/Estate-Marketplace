from django.contrib import admin
from . import models


@admin.register(models.RoomType,models.Facilitie,models.Amenity,models.HouseRule)  # as the other models only have name as common so we put
class ItemAdmin(admin.ModelAdmin):  # them in the same admin class which only has a name

    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

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
                )
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
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
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    ordering = ("name", "price", "bedrooms")

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_facilities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = (
        "city",  # "^city"/"=city"/"@city" (doc)
        "host__username",  # __ to access username of host which is in rooms
    )

    filter_horizontal = (  # only for many to many relationships
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        # print(obj)
        # print(obj.amenities)
        # print(obj.amenities.all())
        # return "Potato"
        return obj.amenities.count()
    
    count_amenities.short_description = "hahaaha"
    
    def count_facilities(self, obj):
        return obj.facilities.count()
    
    # def count_room_type(self, obj):       #cant do this as one to many?
    #     return obj.room_type.count()
        

    def count_photos(self, obj):
        return obj.photos.count()       #Photos class has related name photos so can be accessed



@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
