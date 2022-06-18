from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    mobile = models.CharField(db_index=True, max_length=32)

    def __str__(self):
        return self.username
