from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user, verify_email, ProfileView

urlpatterns = [
    
    path('profile/', ProfileView.as_view(), name='profile'),

    
    path('register/', register_user, name='register'),
    path('verify-email/', verify_email, name='verify_email'),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

