from django.db import models
# clubs data from database and present to the user
# Create your models here.

class Hostel(models.Model):
    name = models.CharField(max_length=255)
    amenities = models.TextField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name