from enum import Enum
from django.utils.translation import gettext_lazy as _


class Messages(Enum):
    INVALID_FORMAT = _("Unknown file format")
    IMAGE_SIZE = _("Image size should not be larger than 2MB")
    MIN_VALUE = _('The price should be positive.')