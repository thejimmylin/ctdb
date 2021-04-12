from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class UserCreateApiTestCase(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_creating_a_valid_user_succeeds(self):
        """Test creating a valid user succeeds"""
        payload = {
            'username': 'username',
            'email': 'email@domain.com',
            'password': 'password',
        }
        response = self.client.post(reverse('user:users'), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], payload['username'])
        self.assertEqual(response.data['email'], payload['email'])
        self.assertNotIn('password', response.data)
        user = User.objects.get(**response.data)
        self.assertTrue(user.check_password(payload['password']))

    def test_creating_a_duplicated_user_fails(self):
        """Test creating a duplicated user fails"""
        payload = {
            'username': 'username',
            'email': 'email@domain.com',
            'password': 'password',
        }
        first_response = self.client.post(reverse('user:users'), payload)
        self.assertEqual(first_response.status_code, status.HTTP_201_CREATED)
        seconad_response = self.client.post(reverse('user:users'), payload)
        self.assertEqual(seconad_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test creating a user with a password too short"""
        payload = {
            'username': 'username',
            'email': 'email@domain.com',
            'password': 'abcde',
        }
        response = self.client.post(reverse('user:users'), payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=payload['username'])

    def test_retrieving_a_user_without_auth_fails(self):
        """Test that authentication required for users"""
        res = self.client.get(reverse('user:me'))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
