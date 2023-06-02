# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.
class UserSerializerView(viewsets.ModelViewSet):
    permisssion_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    