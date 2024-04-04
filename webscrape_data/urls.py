from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterBusinessView.as_view(), name='register_business'),
    path('business/<int:vendor_id>/', views.BusinessDetailsView.as_view(), name='business_details'),
    path('business/<int:vendor_id>/rating-reviews/', views.RatingAndReviewsView.as_view(), name='rating_and_reviews'),
    path('add_review/', views.ReviewCreateView.as_view(), name='add_review_api'),
    path('search_reviews/', views.ReviewSearchView.as_view(), name='search_reviews_api'),
    # path('all-businesses/', views.AllBusinessesView.as_view(), name='all_businesses'),
    path('girls-hostels/', views.GirlsHostelListAPIView.as_view(), name='girls-hostels-list'),
    path('girls-hostels/<int:pk>/', views.GirlsHostelDetailAPIView.as_view(), name='girls-hostel-detail'),

    path('boys-hostels/', views.BoysHostelListAPIView.as_view(), name='boys-hostels-list'),
    path('boys-hostels/<int:pk>/', views.BoysHostelDetailAPIView.as_view(), name='boys-hostel-detail'),

    path('girls-pgs/', views.GirlsPgListAPIView.as_view(), name='girls-pgs-list'),
    path('girls-pgs/<int:pk>/', views.GirlsPgDetailAPIView.as_view(), name='girls-pg-detail'),

    path('boys-pgs/', views.BoysPgListAPIView.as_view(), name='boys-pgs-list'),
    path('boys-pgs/<int:pk>/', views.BoysPgDetailAPIView.as_view(), name='boys-pg-detail'),

    path('tiffins/', views.TiffinListAPIView.as_view(), name='tiffins-list'),
    path('tiffins/<int:pk>/', views.TiffinDetailAPIView.as_view(), name='tiffin-detail'),
]
