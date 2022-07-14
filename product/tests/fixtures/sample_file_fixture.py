from io import BytesIO

import pytest
from django.core.files.base import ContentFile
from PIL import Image


@pytest.fixture
def sample_file():
    file = Image.open("product/tests/fixtures/test_image.jpg")
    thumb_io = BytesIO()
    file.save(thumb_io, file.format, quality=60)
    file.close()
    file = ContentFile(thumb_io.getvalue())
    file.content_type = "image/jpeg"
    file.name = "test_image.jpg"
    return file
