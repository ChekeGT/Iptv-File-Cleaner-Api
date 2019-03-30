"""Users app models schema(Object Oriented schema)."""

# Django
from django.db import models

# Models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Authentication User model

    Inherits from AbstractBaseUser and
    adds some extra fields.
    """

    is_premium = models.BooleanField(default=False)

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with this email already exists.'
        }
    )

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']