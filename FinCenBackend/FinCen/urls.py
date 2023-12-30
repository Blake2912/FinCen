from FinCen.views import *
from django.urls import path

urlpatterns = [
    path('Register', RegisterUser.as_view()),
    path('Login', LoginUser.as_view()),
    path('User', GetUser.as_view()),
    path('Asset', AssetInfo.as_view()),
    path('AddAsset', AddAsset.as_view()),
    path('GetAllAssets', GetAllAssets.as_view())
]