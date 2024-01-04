import pytest
from pydantic import ValidationError

from customer.domain.entities import Customer
from customer.domain.exceptions import InvalidPhoneNumberException


def test_customer_create():
    customer = Customer(
        first_name='test',
        last_name='user',
        email='xyz@example.com',
        phone='+25499919191919',
    )

    assert customer
    assert customer.first_name == 'test'
    assert customer.last_name == 'user'
    assert customer.email == 'xyz@example.com'
    assert customer.phone == '+25499919191919'


def test_customer_create_throws_invalid_email_exception():
    with pytest.raises(ValidationError) as exc:
        Customer(
            first_name='test',
            last_name='user',
            email='xyz@exampl',
            phone='+25499919',
        )
    assert isinstance(exc.value, InvalidPhoneNumberException)
