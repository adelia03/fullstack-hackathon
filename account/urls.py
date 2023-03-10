from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterUserView, DeleteUserView, activate_view, ForgotPassword, ForgotPasswordComplete, user_detail, BalanceView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('delete/<str:email>/', DeleteUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('activate/<str:activation_code>/', activate_view),
    path('forgot-password/', ForgotPassword.as_view()),
    path('forgot-password-complete/<str:activation_code>/', ForgotPasswordComplete.as_view()),
    path('user-detail/<str:id>/', user_detail),
    path('balance/', BalanceView.as_view()),
]