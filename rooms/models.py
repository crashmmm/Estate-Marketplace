from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"
        # ordering = ["created"]
        # ordering = ["name"]


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facilitie(AbstractItem):

    """Facilitie Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to='room_photos')
    room = models.ForeignKey(
        "Room", related_name="photos", on_delete=models.CASCADE
    )  # Room is below and py reads top to bottom.

    # "" works as it searches the "" class in this file.
    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User,
        related_name="rooms",  # default was "room_set" so to access room from user - user.room_set.all()
        on_delete=models.CASCADE,
    )
    # can replace "users.User" and still work
    room_type = models.ForeignKey(
        RoomType, 
        related_name="rooms", 
        on_delete=models.SET_NULL, 
        null=True
    )
    amenities = models.ManyToManyField(
        Amenity,
        related_name="rooms",
        blank=True,
    )
    # can replace Amenity with "Amenity" and it would still work
    facilities = models.ManyToManyField(
        Facilitie,
        related_name="rooms",
        blank=True,
    )
    house_rules = models.ManyToManyField(
        HouseRule,
        related_name="rooms",
        blank=True,
    )

    # .when a class has to be displayed as a string dj/py calls __str__
    def __str__(self):  # py/django tries to change every class to str
        return self.name

    def save(self, *args, **kwargs): # overwride save
       self.city = str.capitalize(self.city)
       super(Room, self).save(*args, **kwargs) # Call the real save() method

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return all_ratings / len(all_reviews)
