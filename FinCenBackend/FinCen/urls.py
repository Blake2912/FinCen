from FinCen.views import *
from django.urls import path

urlpatterns = [
    path('User/Register', RegisterUser.as_view()),
]