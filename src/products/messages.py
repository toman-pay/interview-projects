from enum import Enum
from django.utils.translation import gettext_lazy as _


class Messages(Enum):
    INVALID_FORMAT = _("unknown file format")