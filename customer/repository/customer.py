from typing import Sequence

from customer.repository.base import AbstractCustomerRepository
from customer.domain.entities import Customer as CustomerEntity
from customer.models import Customer


class CustomerRepository(AbstractCustomerRepository):
    def insert(self, obj: CustomerEntity) -> CustomerEntity:
        customer = Customer.objects.create(
            **obj.dict(),
        )
        return CustomerEntity(**customer.__dict__)

    def update(self, obj: CustomerEntity) -> CustomerEntity:
        Customer.objects.filter(id=obj.id).update(**obj.dict())
        customer = Customer.objects.get(id=obj.id)
        return Customer(**customer.__dict__)

    def get_by_id(self, customer_id) -> CustomerEntity | None:
        if customer := Customer.objects.filter(id=customer_id).first():
            return CustomerEntity(**customer.__dict__)

    def delete(self, customer_id) -> None:
        Customer.objects.get(id=customer_id).delete()

    def list(self) -> Sequence[CustomerEntity] | None:
        customers = Customer.objects.all()
        return [
            CustomerEntity(**customer.__dict__)
            for customer in customers
        ]
