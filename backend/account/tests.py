from django.test import TestCase
from django.contrib.auth import get_user_model
from account.models import User

UserModel = User

class UserModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = UserModel.objects.create_user(
            
            email="test@example.com",
            name="Test User",
            password="password123"
        )

    def test_create_user(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.name, "Test User")
        self.assertTrue(self.user.check_password("password123"))
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)

    def test_create_superuser(self):
        admin_user = UserModel.objects.create_superuser(
            email="admin@example.com",
            name="Admin User",
            password="adminpassword123"
        )
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)
