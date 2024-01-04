import pytest
from pytest_factoryboy import register

from customer.repository.customer import CustomerRepository
from factories import CustomerFactory

register(CustomerFactory, name='customer_factory')


@pytest.fixture
def customer_repository():
    return CustomerRepository()
