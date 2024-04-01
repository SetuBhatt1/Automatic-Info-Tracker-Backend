from django.shortcuts import render
import requests
from api.models import User

from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import EmailMessage



class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f"{settings.FRONTEND_URL}/reset-password/{uidb64}/{token}/"

            subject = "Password Reset Request"
            message = render_to_string('email/password_reset_email.html', {
                'user': user,
                'reset_url': reset_url,
            })

            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            return JsonResponse({'message': 'Password reset email sent.'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Check this in your Django console
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer


# Get All Routes

@api_view(['GET', 'POST'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
        'api/login',
        'api/register'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

