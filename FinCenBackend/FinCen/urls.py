from FinCen.views import *
from django.urls import path

urlpatterns = [
    path('Register', RegisterUser.as_view()),
    path('Login',LoginUser.as_view())
]