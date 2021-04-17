from django.urls import path
from .views import register

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
]