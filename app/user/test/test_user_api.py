"""
Tests for user api
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    """Create and return a new user"""
    
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test the public features of the user API."""
    
    def setUp(self):
        self.client = APIClient();
    
    def test_create_user_success(self):
        """Test creating a user successful."""
        paylod = {
            'email': 'exst@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, paylod)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)     
        user.get_user_model().objects.get(email=payload('email'))
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
        
    def test_user_with_email_exists_error(self):
        """Test error return if user with email exist."""
        payload = {
            'email': 'exst@example.com',
            'password': 'testpass123',
            'name': 'Test Name',  
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_password_too_short_error(self):
        """Test an error is return is password less than 5 char."""
        payload = {
            'email': 'exst@example.com',
            'password': 'test',
            'name': 'Test Name',  
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exist)
