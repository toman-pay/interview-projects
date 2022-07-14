import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model

from product.tests.fixtures import sample_file, ProductImageFactory

register(ProductImageFactory)


@pytest.fixture
def api_client(db):
    client = APIClient()
    client.force_authenticate(user=get_user_model().objects.create(username='mari'))
    return client
