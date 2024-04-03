from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterBusinessView.as_view(), name='register_business'),
    path('business/<int:vendor_id>/', views.BusinessDetailsView.as_view(), name='business_details'),
    path('business/<int:vendor_id>/rating-reviews/', views.RatingAndReviewsView.as_view(), name='rating_and_reviews'),
    path('add_review/', views.ReviewCreateView.as_view(), name='add_review_api'),
    path('search_reviews/', views.ReviewSearchView.as_view(), name='search_reviews_api'),
]
