from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User  # Import the User model
from rest_framework import permissions  # Import the permissions module
from .serializers import UserSerializer  # Import the UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
