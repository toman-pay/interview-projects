from django.db import models

from apps.file.models import AbstractFileModel


class SimpleFile(AbstractFileModel):
    """
    File that has relation one-to-one which relation describe in target table not here.
    For example banner-image file which are related to a post in our blog.
    """
    pass


class ProductFile(AbstractFileModel):
    """
    File that are belonged to product images.
    """
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='files')


class UserProfileImage(AbstractFileModel):
    """
    User's profile pictures. each user can have multiple profile pictures, like Telegram.
    """
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='profiles')
