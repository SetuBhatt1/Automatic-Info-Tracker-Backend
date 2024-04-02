from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterBusinessView.as_view(), name='register_business'),
    path('business/<int:vendor_id>/', views.BusinessDetailsView.as_view(), name='business_details'),
    path('business/<int:vendor_id>/rating-reviews/', views.RatingAndReviewsView.as_view(), name='rating_and_reviews'),
]
