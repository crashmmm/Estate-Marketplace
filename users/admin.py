from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)                    #registers and controlls this model
class CustomUserAdmin(UserAdmin):   #this class                                     #also we are inheriting here

    """Custom user Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

# without using decoratore we can also write like this 
# admin.site.register(models.User, CustomUserAdmin)