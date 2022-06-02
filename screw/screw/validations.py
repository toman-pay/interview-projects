from rest_framework.exceptions import ValidationError


def file_size_validation(file):
    limit = 2 * 1024 * 1024
    if file.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')
