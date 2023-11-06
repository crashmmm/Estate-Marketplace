from django.db import models
from core import models as core_models

# Create your models here.


class review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    cleanliness = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):               #function in models as func may be used by others like users etc
        avg = (                             #if func only for admin write func in admin only
            self.accuracy +
            self.cleanliness +
            self.communication +
            self.location +
            self.check_in +
            self.value
            )/6
        return round(avg, 2)
    rating_average.short_description = 'AVG.'
