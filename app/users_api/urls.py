from django.contrib import admin
from django.urls import path, include

from .views import UserDetailsAPIView, ProfileAPIView

urlpatterns = [
    path('', UserDetailsAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view())
]