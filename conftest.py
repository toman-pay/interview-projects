import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from product.tests.fixtures import sample_file, ProductImageFactory

register(ProductImageFactory)


@pytest.fixture
def api_client():
    return APIClient
