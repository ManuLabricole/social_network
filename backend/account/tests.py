from .forms import SignupForm
from django.test import TestCase
from account.models import User
from .forms import SignupForm

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


class SignupFormTest(TestCase):
    def test_valid_form(self):
        # Create a dictionary with valid data for the form
        form_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }

        form = SignupForm(data=form_data)

        # Assert that the form is valid
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        # Create a dictionary with mismatched passwords
        form_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'password1': 'securepassword123',
            'password2': 'differentpassword456',
        }

        form = SignupForm(data=form_data)

        # Assert that the form is not valid due to password mismatch
        self.assertFalse(form.is_valid())

    def test_missing_required_fields(self):
        # Create a dictionary with missing required fields
        form_data = {
            'email': 'test@example.com',
            'name': '',  # Missing name
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }

        form = SignupForm(data=form_data)

        # Assert that the form is not valid due to missing required fields
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        # Create a dictionary with an invalid email format
        form_data = {
            'email': 'invalid-email',  # Invalid email format
            'name': 'Test User',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }

        form = SignupForm(data=form_data)

        # Assert that the form is not valid due to an invalid email format
        self.assertFalse(form.is_valid())
