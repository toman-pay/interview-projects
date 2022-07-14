import factory
import pytest

from django.core.files.base import ContentFile


@pytest.fixture
def sample_file():
    return ContentFile(
        factory.django.ImageField()._make_data({"width": 1024, "height": 768}), "test_image.jpg"
    )
