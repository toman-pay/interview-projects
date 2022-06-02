from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from escrow_account.models.base_model import BaseModel
from escrow_account.models.uuid_model import UUIDModel
from identity.managers.user_model_manager import UserModelManager


class UserModel(AbstractBaseUser, BaseModel, UUIDModel):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), null=True, blank=True, max_length=128)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    # user object managers
    objects = UserModelManager()
    all_objects = UserModelManager(alive_only=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = "user"
