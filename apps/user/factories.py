import factory

from django.contrib.auth import get_user_model

User = get_user_model()


class BaseUserFactory(factory.Factory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    username = factory.Faker('username')

    class Meta:
        model = User


class UserFactory(BaseUserFactory):
    admin = False


class AdminFactory(factory.Factory):
    admin = True
