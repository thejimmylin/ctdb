
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class UserUpdateApiTestCase(TestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='username',
            email='email@domain.com',
            password='password',
            first_name='firstname',
            last_name='lastname',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieving_me_with_auth_succeeds(self):
        """Test retrieving a user with auth succeed"""
        res = self.client.get(reverse('user:me'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
        })

    def test_post_me_fails(self):
        """Test POST me fails"""
        res = self.client.post(reverse('user:me'), {})
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_me_succeed(self):
        """Test updating the user profile for authenticated user"""
        payload = {
            'first_name': 'newfirstname',
            'last_name': 'newlastname',
            'password': 'new_password',
        }
        res = self.client.patch(reverse('user:me'), payload)
        self.user.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.first_name, payload['first_name'])
        self.assertEqual(self.user.last_name, payload['last_name'])
        self.assertTrue(self.user.check_password(payload['password']))
