from typing import Optional
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class AuthService:
    @staticmethod
    def create_user(email, password, first_name, last_name, **extra_fields) -> User:
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        return user

    @staticmethod
    def authenticate_user(email, password) -> Optional[User]:
        return authenticate(email=email, password=password)

    @staticmethod
    def get_jwt_tokens(user: User) -> dict:
        refresh = RefreshToken.for_user(user)
        return {
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token)
        }
