import factory

from product.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker("text", max_nb_chars=50)
    description = factory.Faker("text", max_nb_chars=100)
    price = factory.Faker('pyint', min_value=100, max_value=1000)

