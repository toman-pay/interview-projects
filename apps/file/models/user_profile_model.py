from django.db import models

from apps.file.models import AbstractFileModel


class UserProfileImage(AbstractFileModel):
    """
    User's profile pictures. each user can have multiple profile pictures, like Telegram.
    """
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='profiles')
