from django.conf import settings
from django.core.exceptions import ValidationError


def validate_file_size(document):
    if document.size > settings.MAX_FILE_SIZE:
        raise ValidationError(
            f"File size is greater than {int(settings.MAX_FILE_SIZE / 1024 / 1024)} MB."
        )
