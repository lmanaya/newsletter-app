from django.test import TestCase
from django.urls import reverse
from .models import User

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.url = reverse("register")

    def test_register_user_success(self):
        """
        Test for successful user registration.
        """
        data = {
            "email": "admin@newsletter.com",
            "password": "p@ssw0rd",
            "first_name": "Admin",
            "last_name": "Newsletter"
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {"success": "User registered successfully!"})
        self.assertTrue(User.objects.filter(email=data["email"]).exists())

    def test_register_user_invalid_data(self):
        """
        Test for failed user registration.
        """
        data = {
            "email": "email",
            "password": "wr0n6Dat4",
            "first_name": "Wrong",
            "last_name": "Data"
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(User.objects.filter(first_name="Wrong").exists())

    def test_register_user_invalid_email_data(self):
        """
        Test for failed user registration by duplicated email.
        """
        self.test_register_user_success()

        data = {
            "email": "admin@newsletter.com",
            "password": "p@ssw0rd",
            "first_name": "Admin",
            "last_name": "Newsletter"
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)
        self.assertTrue(User.objects.filter(email=data["email"]).exists())

class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        self.url = reverse("login")

    def register_user(self, data):
        """
        Helper method to register a user.
        """
        registration_url = reverse("register")
        response = self.client.post(registration_url, data)
        return response

    def test_login_user_success(self):
        """
        Test for successful user authentication.
        """
        data = {
            "email": "admin@newsletter.com",
            "password": "p@ssw0rd",
            "first_name": "Admin",
            "last_name": "Newsletter"
        }
        self.register_user(data=data)
        user = User.objects.get(email=data["email"])
        user.is_active = True
        user.save()

        response = self.client.post(
            self.url,
            { "email": data["email"], "password": data["password"]}
        )

        self.assertEqual(response.status_code, 200)

    def test_login_inactive_user(self):
        """
        Test for inactive user authentication.
        """
        data = {
            "email": "admin@newsletter.com",
            "password": "p@ssw0rd",
            "first_name": "Admin",
            "last_name": "Newsletter"
        }
        self.register_user(data=data)

        response = self.client.post(
            self.url,
            { "email": data["email"], "password": data["password"]})

        self.assertEqual(response.status_code, 400)
