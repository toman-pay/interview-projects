from django.urls import reverse
from django.test import override_settings
from rest_framework import status

from product.models import ProductImage

URL = reverse("product-image-create")


def test_product_image_viewset_with_valid_image(api_client, db, sample_file):
    response = api_client().post(URL, data={"image": sample_file})
    assert response.status_code == status.HTTP_201_CREATED
    assert ProductImage.objects.count() == 1


@override_settings(MAX_FILE_SIZE=1)
def test_product_image_viewset_with_large_image(api_client, db, sample_file):
    response = api_client().post(URL, data={"image": sample_file})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert ProductImage.objects.count() == 0
