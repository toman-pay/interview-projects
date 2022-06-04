import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class BaseModel(models.Model):
    """
    Base model for inheritence for another models.
    """
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    is_deleted = models.BooleanField(_("is_deleted"), default=False)
    # objects = models.Manager() => The default manager.
    objects = BaseManager()

    class Meta:
        abstract = True

