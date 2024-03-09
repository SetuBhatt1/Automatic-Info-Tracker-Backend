from django.urls import path
from .views import get_hostels_data

urlpatterns = [
    path('api/get_hostels_data/', get_hostels_data, name='get_hostels_data'),
]
