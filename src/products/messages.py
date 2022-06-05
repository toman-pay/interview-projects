from enum import Enum
from django.utils.translation import gettext_lazy as _


class Messages(Enum):
    INVALID_FORMAT = _("unknown file format")
    IMAGE_SIZE = _("image size should not be larger than 2MB")
    MIN_VALUE = _('Ensure this value is greater than {min_value}.')