from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProjectSerializer
from .models import project
from rest_framework.response import Response

# Create your views here.

class ProjectView(APIView):
    def get(self, request):
        output = [
            {
                'id': output.id,
                "employee": output.employee,
                "department": output.department
             }
             for output in project.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
