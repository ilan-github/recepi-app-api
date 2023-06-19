"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""
    
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email, 
            password = password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """Test email is normalized to a new user."""
        sample_examples = [
            ['Test1@EXAMPLE.com', 'Test1@example.com'], 
            ['test2@Example.com', 'test2@example.com'], 
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'], 
            ['text4@example.COM', 'text4@example.com'], 
        ]
        
        for email, expected in sample_examples:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')
    
    def test_create_super_user(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@exmple.com', 'text123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)