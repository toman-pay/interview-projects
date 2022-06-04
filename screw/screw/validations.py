from rest_framework.exceptions import ValidationError


def upload_limit_validation(files, max_count):
    if len(files) > max_count:
        raise ValidationError('Sorry! maximum number of images to upload is 5')


def file_size_validation(file):
    limit = 2 * 1024 * 1024
    if file.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')
