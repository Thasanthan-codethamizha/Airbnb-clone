from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    GENDER_MALE ="male"
    GENDER_FEMALE ="female"
    GENDER_OTHER ="other"

    GENDER_CHOICES=(
        (GENDER_MALE,"Male"),
        (GENDER_FEMALE,"Female"),
        (GENDER_OTHER,"Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_TAMIL ="ta"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH,"Enlgish"),
        (LANGUAGE_TAMIL,"Tamil"),
    )

    CURRENCY_USD ="usd"
    CURRENCY_LKR = "lkr"

    CURRENCY_CHOICES = (
        (CURRENCY_USD,"USD"),
        (CURRENCY_LKR,"LKR"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,blank=True,null=True,max_length=10)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True,blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES,blank=True,null=True,max_length=10)
    currency = models.CharField(choices=CURRENCY_CHOICES,blank=True,null=True,max_length=10)
    superhost = models.BooleanField(default=False)
