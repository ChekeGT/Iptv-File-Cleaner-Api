"""Users app serializers."""

# Django REST Framework
from rest_framework import serializers

# Django
from django.contrib.auth import authenticate, password_validation

# Models
from .models import User

# Validators
from rest_framework.validators import UniqueValidator


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Metadata class."""

        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_premium',
        )
        read_only_fields = (
            'is_premium',
        )


class UserSignupSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all()
            )
        ],
        min_length=5,
        max_length=250
    )
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all()
            )
        ],
        max_length=20
    )
    password = serializers.CharField(
        min_length=8,
        max_length=200,
    )
    password_confirmation = serializers.CharField(
        min_length=8,
        max_length=200
    )
    first_name = serializers.CharField(
        min_length=3,
        max_length=200
    )
    last_name = serializers.CharField(
        min_length=3,
        max_length=300
    )

    def validate(self, data):
        """Validates password and password confirmation are equal."""

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:

            raise serializers.ValidationError('Password and password confirmation need to be equal.')

        data.pop('password_confirmation')
        password_validation.validate_password(password)

        return data

    def create(self, validated_data):
        """Manages creating the user with the given data."""

        user = User.objects.create_user(**validated_data)

        return user