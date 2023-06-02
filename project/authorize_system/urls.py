from django.urls import path
from .views import *


urlpatterns = [
    path('login/',LoginAPI, name='login'),
    path('signup',SignupAPI, name='signup'),
    path('user/',get_user_data),
]
