from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('login/', views.LoginView.as_view(), name='auth_login'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='auth_forgot_password'),
    # path('send-email/',views.send_email_client, name='send_email_client'),
    path('', views.getRoutes),
]
