from django.db import models
from db_connection import db

# Create your models here.

# using db, we can register our first model
tiffin_collection = db["Tiffin"]
