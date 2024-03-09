from django.urls import path
from . import views

# url-configurations
urlpatterns = [
    path("girls-hostels/", views.get_hostel),
]
