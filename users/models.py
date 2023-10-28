from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):       #inheriting from per writtern django Abstract user and extending it

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_MALE, "Female"),
        (GENDER_MALE, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # .null is for the database and blank is for the form
    # .we dont have to migrate while adding gender choices bcos its a
    # change only for the form and not the database
    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True
    )
    bio = models.TextField(blank=True)
    birthdate = models.DateField( blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True
    )

    superhost = models.BooleanField(default=False)

    # .as this is extended from the preexisting users django has the str conversion of the class to selfname was probably preconfigured
    # def __str__(self):
    #         return self.name