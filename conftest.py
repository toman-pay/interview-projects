import pytest
from rest_framework.test import APIClient

from product.tests.fixtures import sample_file


@pytest.fixture
def api_client():
    return APIClient
