from rest_framework import serializers
from .models import CustomUserManager, CustomUser

class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUserManager
        fields = ['id','email', 'password']

class SignupSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'firstname', 'lastname', 'email', 'password']
