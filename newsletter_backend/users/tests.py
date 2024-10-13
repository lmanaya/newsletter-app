from django.test import TestCase
from django.urls import reverse
from .models import User


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.url = reverse('register')

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
        self.assertTrue(User.objects.filter(email=data['email']).exists())

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
        self.assertFalse(User.objects.filter(first_name="John").exists())


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
        self.assertTrue(User.objects.filter(email=data['email']).exists())
