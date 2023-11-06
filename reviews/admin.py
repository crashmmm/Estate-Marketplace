from django.contrib import admin
from . import models


@admin.register(models.review)
class ReviewAdimin(admin.ModelAdmin):

    """ Review Admin Definition """

    list_display = (
        "__str__",
        "rating_average"
    )
