from rest_framework import serializers
from .models import project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields = ['id', 'employee', 'department']


