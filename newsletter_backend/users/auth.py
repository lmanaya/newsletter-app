from .models import User


class AuthService:
    @staticmethod
    def create_user(email, password, first_name, last_name, **extra_fields):
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        return user
