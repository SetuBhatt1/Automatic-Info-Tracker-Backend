from django.db import models


# Create your models here.

class HostelPgCommon(models.Model):
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

    name = models.CharField(max_length=100, default="Name")
    email = models.EmailField(default="Email")
    phone = models.CharField(max_length=15, default="Phone")
    address = models.TextField(max_length=150, default="Address")
    room_type = models.CharField(max_length=1, choices=room_type_choices, default="N")
    room_shared = models.CharField(max_length=1, choices=yes_no_choices, default="Y")
    amenities = models.TextField(default="Amenities")
    in_time = models.TimeField(default="20:00:00")
    warden_present = models.CharField(max_length=1, choices=yes_no_choices, default="N")
    no_of_wardens = models.IntegerField(default="0")
    food_included = models.CharField(max_length=1, choices=yes_no_choices, default="N")
    longitude = models.DecimalField(max_digits=10, decimal_places=8, default=0.0)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, default=0.0)
    security_present = models.CharField(max_length=1, choices=yes_no_choices, default="N")
    for_gender = models.CharField(max_length=1, choices=boy_girl_choices, default="G")
    rules = models.TextField(default="Rules")
    rating = models.FloatField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    total_reviews = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)  # Assuming multiple URLs are stored as a string

    class Meta:
        abstract = True


class GirlsHostel(HostelPgCommon):
    pass


class BoysHostel(HostelPgCommon):
    pass


class GirlsPg(HostelPgCommon):
    pass


class BoysPg(HostelPgCommon):
    pass


class Tiffin(models.Model):
    yes_no_choices = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    veg_nonveg_choices = [
        ('V', 'Veg'),
        ('NV', 'Non-Veg')
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="Name")
    email = models.EmailField(default="Email")
    phone = models.CharField(max_length=15, default="Phone")
    address = models.TextField(max_length=150, default="Address")
    longitude = models.DecimalField(max_digits=10, decimal_places=8, default=0.0)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, default=0.0)
    type_of_food = models.CharField(max_length=2, choices=veg_nonveg_choices, default="V")
    menu = models.FileField(upload_to='pdfs/')
    delivers_to_loc = models.TextField(max_length=150, default="Delivering Location")
    OpensAt = models.TimeField()
    ClosesAt = models.TimeField()


class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, default="Full Name")
    email = models.EmailField(default="Email")
    message = models.TextField(default="Message")


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    experience = models.TextField(default="Experience")
    photos = models.ImageField(upload_to='images/')
    rating = models.FloatField()


class Vendor(models.Model):
    select_business = [
        ('H', 'Hostel'),
        ('Pg', 'Pg'),
        ('T', 'Tiffin')
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="Name")
    email = models.EmailField(default="Email")
    password = models.CharField(max_length=100, default="Password")
    phone = models.CharField(max_length=15, default="Phone")
    type_of_business = models.CharField(max_length=2, choices=select_business)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="Name")
    email = models.EmailField(default="Email")
    password = models.CharField(max_length=100, default="Password")
    phone = models.CharField(max_length=15, default="Phone")
    university_name = models.CharField(max_length=200)
