import factory
from django.core.files.base import ContentFile

from product.models import ProductImage
from .product_factory import ProductFactory


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 1024, "height": 768}), "example.jpg"
        )
    )
    product = factory.SubFactory(ProductFactory)
