from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facilitie, models.Amenity, models.HouseRule) #as the other models only have name as common so we put 
class ItemAdmin(admin.ModelAdmin):                                                    #them in the same admin class which only has a name 

    """ Item Admin Definition """

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    pass

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass