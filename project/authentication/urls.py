from django.urls import path
from .views import  SignupAPI, LoginAPI

urlpatterns = [
    # path('', ),
    path('signup', SignupAPI.as_view(), name='signup'),
    path('login', LoginAPI.as_view(), name='login'),
]
