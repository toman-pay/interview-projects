"""
    This module is written to validate the request data
"""

from django.core.exceptions import ValidationError
from interview_task.settings import IMAGE_SIZE_LIMIT


def validate_image_size(images):
    """
       This method checks the size of the image before upload
    """
    for image in images:
        image_size = image.size

        if image_size > IMAGE_SIZE_LIMIT*1024*1024:
            raise ValidationError(
                f"file with name : {image.name} is more than {IMAGE_SIZE_LIMIT}Mb")
