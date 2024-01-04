from customer.domain.entities import Customer as CustomerEntity
from customer.use_cases.base import AbstractCustomerUseCase


class CustomerUseCase(AbstractCustomerUseCase):
    def __init__(self, customer_repo):
        self.repo = customer_repo

    def get_by_id(self, customer_id):
        return self.repo.get_by_id(customer_id)

    def insert(self, customer: CustomerEntity):
        return self.repo.insert(customer)

    def update(self, customer: CustomerEntity):
        return self.repo.update(customer)

    def delete(self, customer_id):
        self.repo.delete(customer_id)

    def list(self):
        return self.repo.list()
