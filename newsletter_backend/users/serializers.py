from rest_framework import serializers
from .models import User
from .auth import AuthService


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        user = AuthService.create_user(**validated_data)
        return user
