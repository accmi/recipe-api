from django.test import TestCase
from django.contrib.auth import get_user_model


EMAIL = 'test@email.test'
PASSWORD = '12345678'


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Should creat a new user with email successfully"""
        user = get_user_model().objects.create_user(
            email=EMAIL,
            password=PASSWORD,
        )

        self.assertEqual(user.email, EMAIL)
        self.assertTrue(user.check_password(PASSWORD))

    def test_new_user_email_normalizes(self):
        """Test the email for a new user is normalized"""
        user = get_user_model().objects.create_user(EMAIL, PASSWORD)

        self.assertEqual(user.email, EMAIL.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email=EMAIL,
            password=PASSWORD,
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
