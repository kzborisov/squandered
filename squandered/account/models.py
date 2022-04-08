from django.contrib.auth import models as auth_models
from django.contrib.auth import validators as auth_validators
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class CustomUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 150

    username_validator = auth_validators.UnicodeUsernameValidator()
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = auth_models.UserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 150
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 150
    LAST_NAME_MIN_LENGTH = 2

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        ]
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        ]
    )
    # TODO: Add additional profile info like images, etc.
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
