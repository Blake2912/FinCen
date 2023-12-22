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

class UserResponseSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    api_key = serializers.CharField()

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop(nameof(User.password), None)
        return rep
