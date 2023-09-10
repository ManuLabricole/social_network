import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionManager, PermissionsMixin, UserManager


from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.

        Args:
            email (str): The email address of the user.
            password (str): The user's password.
            **extra_fields: Additional fields to set on the user model.

        Raises:
            ValueError: If the email is not provided.

        Returns:
            User: The newly created user instance.
        """
        if not email:
            raise ValueError('The given email must be set')

        # Normalize the email address to ensure consistent formatting.
        email = self.normalize_email(email)

        # Create a new user instance with the provided email and extra fields.
        user = self.model(email=email, name=name, **extra_fields)

        # Set the user's password using Django's password hashing mechanism.
        user.set_password(password)

        # Save the user to the database using the database specified in self._db.
        user.save(using=self._db)

        # Return the created user instance.
        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        """
        Create a standard user with the given email and password.

        Args:
            name (str): The name of the user.
            email (str): The email address of the user.
            password (str, optional): The user's password.
            **extra_fields: Additional fields to set on the user model.

        Returns:
            User: The newly created user instance.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # Call the _create_user method to create and save the user.
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        """
        Create a superuser with the given email and password.

        Args:
            name (str): The name of the superuser.
            email (str): The email address of the superuser.
            password (str, optional): The superuser's password.
            **extra_fields: Additional fields to set on the user model.

        Returns:
            User: The newly created superuser instance.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Call the _create_user method to create and save the superuser.
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
