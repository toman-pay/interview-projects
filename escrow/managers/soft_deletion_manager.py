from django.db import models
from escrow.managers.soft_deletion_queryset import SoftDeletionQuerySet


class SoftDeletionManager(models.Manager):
    """ Manager to support soft deletion in our BaseModel"""

    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        """This method is used to return alive objects if we want alive_only object else all of them."""
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        """This method allows to really delete an object :|"""
        return self.get_queryset().hard_delete()
