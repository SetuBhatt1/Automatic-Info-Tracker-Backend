from django.db import models
from db_connection import db

# Create your models here.

# using db, we can register our first model
tiffin_collection = db["Tiffin"]


from django.db import models


class Hostel(models.Model):
    room_type_choices = [
        ('A', 'AC Room'),
        ('N', 'Non AC Room')
    ]

    yes_no_choices = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]

    boy_girl_choices = [
        ('B', 'Boy'),
        ('G', 'Girl')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="Default Name")
    phone = models.CharField(max_length=15)
    address = models.TextField()
    room_type = models.CharField(max_length=1, choices=room_type_choices)
    room_shared = models.CharField(max_length=1, choices=yes_no_choices)
    amenities = models.TextField(default="Default Amentities")
    in_time = models.TimeField()
    warden_present = models.CharField(max_length=1, choices=yes_no_choices)
    no_of_wardens = models.IntegerField()
    food_included = models.CharField(max_length=1, choices=yes_no_choices)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    security_present = models.CharField(max_length=1, choices=yes_no_choices)
    for_boy_or_girl = models.CharField(max_length=1, choices=boy_girl_choices)
    rules = models.TextField(default="Default Rules")

    rating = models.FloatField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    total_reviews = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)  # Assuming multiple URLs are stored as a string

    class Meta:
        abstract = True
class GirlsHostel(Hostel):
    pass


class BoysHostel(Hostel):
    pass


class Pg(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    total_reviews = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)  # Assuming multiple URLs are stored as a string
    video = models.URLField(blank=True, null=True)
    opening_time = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    doc_id = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    web_url = models.URLField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    scraped_at = models.DateTimeField(blank=True, null=True)


class GirlsPg(Pg):
    # Additional fields specific to GirlsHostel if any
    pass


class BoysPg(Pg):
    # Additional fields specific to BoysHostel if any
    pass
