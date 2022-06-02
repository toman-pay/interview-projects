from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager

from escrow_account.manager.base_model_manager import BaseModelManager


class UserEntityManager(BaseModelManager, UserManager):
    """
    Customized UserManager adapted to the removal of 'username' field.
    """

    def _create_user(self, username=None, email=None, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)
