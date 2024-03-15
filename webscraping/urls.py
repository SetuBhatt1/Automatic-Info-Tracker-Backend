from django.urls import path
from . import views


urlpatterns = [
    path('tiffins/', views.get_all_tiffins, name='get_all_tiffins'),
    path('girls-hostels/', views.get_all_girls_hostel),
    path('boys-hostels/', views.get_all_boys_hostels),
]
