from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    # path('get_hostels_data/', get_hostels_data, name='get_hostels_data'),
    path('add/',views.add_tiffin),
    path('show/',views.get_all_tiffins)
]
