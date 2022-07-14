import json

import pytest
from django.urls import reverse
from django.test import override_settings
from rest_framework import status

from product.models import Product

URL = reverse("product-create")


def test_creating_product_with_valid_data(api_client, data):
    response = api_client.post(URL, data=data)
    assert response.status_code == status.HTTP_201_CREATED

    response_json = json.loads(response.content)
    assert response_json["success"] is True
    assert Product.objects.count() == 1


def test_creating_product_with_nonpositive_price(api_client, data):
    data["price"] = 0
    response = api_client.post(URL, data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response_json = json.loads(response.content)
    assert response_json["success"] is False
    assert response_json["errors"] is not None
    assert Product.objects.count() == 0


@pytest.mark.skip("to be fixed")
def test_creating_a_product_with_multiple_files(product_image_factory, api_client, data):
    images = product_image_factory.create_batch(2, product=None)
    data["imageids"] = [i.id for i in images]
    response = api_client.post(URL, data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.count() == 1

    created_product = Product.objects.last()
    for image in images:
        image.refresh_from_db()
        assert image.product == created_product


@pytest.mark.skip("to be fixed")
@override_settings(MAX_NUMBER_OF_FILES_PER_PRODUCT=2)
def test_creating_a_product_with_many_files(product_image_factory, api_client, data):
    images = product_image_factory.create_batch(3)
    data["imageids"] = [i.id for i in images]
    response = api_client.post(URL, data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Product.objects.count() == 0


@pytest.fixture
def data():
    return {
        "title": "product 1",
        "description": "product description",
        "price": 10,
    }
