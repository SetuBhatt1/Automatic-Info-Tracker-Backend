from django.db import models
from db_connection import db

# Create your models here.

# using db, we can register our first model
tiffin_collection = db["Tiffin"]


class Hostel(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    total_reviews = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    images = models.TextField(blank=True, null=True) # Assuming multiple URLs are stored as a string
    video = models.URLField(blank=True, null=True)
    opening_time = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    doc_id = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    web_url = models.URLField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    scraped_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class GirlsHostel(Hostel):
    # Additional fields specific to GirlsHostel if any
    pass

class BoysHostel(Hostel):
    # Additional fields specific to BoysHostel if any
    pass

