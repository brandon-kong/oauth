from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

import uuid

from .managers import UserManager

class User(AbstractUser):
    """
    User model for authentication
    """
    
    id = models.BigAutoField(primary_key=True, editable=False)

    implicit_id = models.UUIDField(
        default = uuid.uuid4,
        unique=True,
        editable = False
    )

    username = None
    email = models.EmailField(_("email address"), unique=True)

    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_user_with_id (self, s: str) -> "User":
        """
        Get user with UUID string
        """

        return User.objects.get(implicit_id=s)
