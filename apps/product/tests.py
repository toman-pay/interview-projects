from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from freezegun import freeze_time
from unittest.mock import patch

User = get_user_model()


class UserTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.username = "test_username"
        cls.password = "test_pass"
        cls.payload = {"username": cls.username, "password": cls.password}

    def test_create_user(self):
        users_count = User.objects.count()
        self.assertEqual(users_count, 0)
        User.objects.create_user(**self.payload)
        users_count = User.objects.count()
        self.assertEqual(first=users_count, second=1, msg="User creation process not working correctly!")

    @freeze_time("2012-01-01 03:00:00", tz_offset=-0)
    def test_login(self):
        User.objects.create_user(**self.payload)
        client = APIClient()
        response = client.post('/api/token/', self.payload, format='json')
        data = response.data
        self.assertTrue(expr=all([k in ["access", "refresh"] for k in data.keys()]),
                        msg="access and refresh token not exist in login response!")
        self.assertEqual(len(data['access'].split(".")), 3)
        self.assertEqual(len(data['refresh'].split(".")), 3)
        # TODO: do JWT validation .........
