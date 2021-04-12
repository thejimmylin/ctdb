from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class TokenCreateApiTestCase(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_creating_a_token_with_valid_credentials(self):
        """Test creating a token with valid credentials"""
        payload = {
            'username': 'username',
            'email': 'email@domain.com',
            'password': 'password',
        }
        User.objects.create_user(**payload)
        response = self.client.post(reverse('user:tokens'), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_creating_a_token_with_invalid_credentials(self):
        """Test creating a token with invalid credentials"""
        credentials = {
            'username': 'username',
            'email': 'email@domain.com',
            'password': 'password',
        }
        User.objects.create_user(**credentials)
        payload = {
            'username': 'username',
            'email': 'email@domain.com',
            'password': 'wrong_password',
        }
        response = self.client.post(reverse('user:tokens'), payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_creating_a_token_with_a_not_existing_user(self):
        """Test creating a token with a not existing user"""
        payload = {
            'username': 'username',
            'email': 'email@domain.com',
            'password': 'password',
        }
        response = self.client.post(reverse('user:tokens'), payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_creating_a_token_with_incomplete_credentials(self):
        """Test creating a token with incomplete credentials"""
        payload = {
            'username': 'username',
            'password': '',
        }
        response = self.client.post(reverse('user:tokens'), payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)
