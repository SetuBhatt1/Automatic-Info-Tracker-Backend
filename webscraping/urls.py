from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    # path('get_hostels_data/', get_hostels_data, name='get_hostels_data'),
    path('tiffin/add',views.add_tiffin),
    path('tiffin/get',views.get_all_tiffins)
]
