from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from products.validators import validate_image_extension, validate_image_size

from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, username=None, **extra_fields):
        """Create and save user with the given email and password"""

        if not email:
            raise ValueError("User should have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create a superuser with the given email and password"""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    email = models.EmailField(
        max_length=255, unique=True, verbose_name='email')
    avatar = VersatileImageField(
        'profile Picture',
        upload_to='profile_pictures', blank=True, null=True,
        ppoi_field='avatar_ppoi',
        default='profile_pictures/{}'.format(settings.DEFAULT_PICTURE),
        validators=[validate_image_extension, validate_image_size]
    )

    phone = models.CharField(max_length=32, blank=True, null=True)
    full_name = models.CharField(max_length=255)

    avatar_ppoi = PPOIField()

    REQUIRED_FIELDS = ['password', 'full_name']
    USERNAME_FIELD = 'email'
    username = None

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_username(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
