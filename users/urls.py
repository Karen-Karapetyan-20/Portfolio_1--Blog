from django.urls import path
from .views import Registration, ProfileUpdate
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView
)

app_name = "users"

urlpatterns = [
    path("reg/", Registration.as_view(), name="reg"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-change/",
         PasswordChangeView.as_view(),
         name="password_change"),
    path("password_change_done/",
         PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path("profile/", ProfileUpdate.as_view(), name="profile"),
]
