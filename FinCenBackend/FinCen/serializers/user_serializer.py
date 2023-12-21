from rest_framework import  serializers
from varname import nameof
from ..models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [nameof(User.user_name), nameof(User.first_name), nameof(User.last_name), nameof(User.email), nameof(User.password)]

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [nameof(User.user_name), nameof(User.password)]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'