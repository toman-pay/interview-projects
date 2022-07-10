import os.path

from django.contrib.auth import get_user_model
from django.test import TestCase
from freezegun import freeze_time
from rest_framework.test import APIClient
# from unittest.mock import patch
User = get_user_model()


class UserTest(TestCase):
    base_api = '/api/v1/'
    username = "test_username"
    password = "test_pass"
    cred_payload = {"username": username, "password": password}

    # @patch('apps.user.model.smt')
    def test_create_user(self):
        users_count = User.objects.count()
        self.assertEqual(users_count, 0)
        User.objects.create_user(**self.cred_payload)
        users_count = User.objects.count()
        self.assertEqual(first=users_count, second=1, msg="User creation process not working correctly!")

    @freeze_time("2012-01-01 03:00:00", tz_offset=-0)
    def test_login(self):
        user = User.objects.create_user(**self.cred_payload)

        # Login manually
        client = APIClient()
        response = client.post('/api/token/', self.cred_payload, format='json')
        data = response.data
        self.assertTrue(expr=all([k in ["access", "refresh"] for k in data.keys()]),
                        msg="access and refresh token not exist in login response!")
        # TODO: do JWT validation in future .........
        self.assertEqual(len(data['access'].split(".")), 3)
        self.assertEqual(len(data['refresh'].split(".")), 3)

        # Whoami?
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {data['access']}")
        r = client.get(os.path.join(self.base_api, 'users/whoami/'))
        self.assertEqual(r.status_code, 200)
        d = r.json()
        self.assertIsInstance(d, dict)
        self.assertEqual(d.get('username'), user.username)

        # refresh my token
        client = APIClient()
        refresh_response = client.post('/api/token/refresh/', data, format='json')
        refresh_data = refresh_response.data
        self.assertTrue(expr=all([k in ["access", "refresh"] for k in refresh_data.keys()]),
                        msg="access and refresh token not exist in login response!")
        self.assertEqual(len(refresh_data['access'].split(".")), 3)
        self.assertEqual(len(refresh_data['refresh'].split(".")), 3)

        # whoami with refreshed token
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh_data['access']}")
        r = client.get(os.path.join(self.base_api, 'users/whoami/'))
        self.assertEqual(r.status_code, 200)
        d = r.json()
        self.assertIsInstance(d, dict)
        self.assertEqual(d.get('username'), user.username)
