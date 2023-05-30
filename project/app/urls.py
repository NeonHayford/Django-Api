from django.urls import path
from .views import ProjectView
# from django.conf.urls import url

urlpatterns = [
    path('api/', ProjectView.as_view(), name='project')
]