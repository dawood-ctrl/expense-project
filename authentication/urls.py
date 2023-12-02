from .views import RegistrationView
from django.urls import path

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),  # Trailing slash and name parameter
]

