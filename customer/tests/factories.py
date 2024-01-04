import uuid

import factory

from customer.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    id = factory.LazyAttribute(lambda s: uuid.uuid4())
    first_name = factory.Faker('pystr')
    last_name = factory.Faker('pystr')
    email = factory.Faker('email')
    phone = '+9551370038'

    class Meta:
        model = Customer
