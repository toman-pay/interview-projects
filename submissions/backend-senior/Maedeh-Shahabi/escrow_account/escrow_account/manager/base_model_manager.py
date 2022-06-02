from django.db import models

from escrow_account.base_constants import BaseConstants
from escrow_account.manager.soft_deletion_queryset import SoftDeletionQuerySet


class BaseModelManager(models.Manager):
    """
    A custom model manager for our base_model
    """

    def __init__(self, *args, **kwargs):
        """
        'alive_only' kwarg is called on objects in each model to return whether alive objects or all of them.
        """
        self.alive_only = kwargs.pop(BaseConstants.alive_only, True)
        super(BaseModelManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        """
        This method is called on each query, to return those objects which are alive(deletion_time=None) or dead
        """
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deletion_time=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        """
        Allows you to really delete an object!
        """
        return self.get_queryset().hard_delete()
