from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .tokens import generate_token, verify_token
from .models import CustomUser

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ProfileSerializer



def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse("User already exists.")

        # Create user as inactive (email not verified yet)
        user = CustomUser.objects.create_user(email=email, password=password)
        user.is_active = False
        user.save()

        # Send email verification
        send_verification_email(user, request)
        return HttpResponse("Registration successful. Please check your email to verify.")

    return render(request, 'accounts/register.html')  # You can customize this template



def send_verification_email(user, request):
    token = generate_token(user.email)
    current_site = get_current_site(request)
    verify_url = f"http://{current_site.domain}{reverse('verify_email')}?token={token}"

    send_mail(
        'Verify your email address',
        f'Click the link to verify your account:\n{verify_url}',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )



def verify_email(request):
    token = request.GET.get('token')
    email = verify_token(token)

    if email:
        try:
            user = CustomUser.objects.get(email=email)
            user.is_active = True
            user.save()
            return HttpResponse(" Email verified successfully. You can now log in.")
        except CustomUser.DoesNotExist:
            return HttpResponse(" User not found.")
    return HttpResponse(" Invalid or expired verification link.")


# 4. DRF Profile View (API)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Block if user email is not verified
        if not user.is_active:
            return Response(
                {"detail": "Please verify your email to access your profile."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Get user profile
        profile = user.profile  # Assuming OneToOneField to CustomUser
        serialized_profile = ProfileSerializer(profile).data

        return Response({
            "email": user.email,
            "profile": serialized_profile
        })
