from django.db import models
from core.models import TimeStampedModel
from django_countries.fields import CountryField
from users.models import User
# Create your models here.
class Room(TimeStampedModel):
    """
    Model representing a room.
    """
    name = models.CharField(max_length=200, help_text="Enter a room name")
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    # room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    # amenities = models.ManyToManyField("Amenity", blank=True)
    # facilities = models.ManyToManyField("Facility", blank=True)
    # house_rules = models.ManyToManyField("HouseRule", blank=True)
    