from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import User
from .auth import AuthService


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        user = AuthService.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    user = UserSerializer(required=False)
    access_token = serializers.CharField(required=False)
    refresh_token = serializers.CharField(required=False)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        email = validated_data.get("email")
        password = validated_data.get("password")

        user = AuthService.authenticate_user(email=email, password=password)
        if not user:
            raise serializers.ValidationError(_("Invalid credentials provided or user inactive."))

        tokens = AuthService.get_jwt_tokens(user)

        validated_data["user"] = user
        validated_data["access_token"] = tokens["access_token"]
        validated_data["refresh_token"] = tokens["refresh_token"]
        return validated_data
