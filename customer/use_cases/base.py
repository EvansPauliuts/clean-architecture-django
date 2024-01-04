from abc import ABC, abstractmethod

from customer.domain.entities import Customer as CustomerEntity


class AbstractCustomerUseCase(ABC):
    @abstractmethod
    def get_by_id(self, customer_id):
        ...

    @abstractmethod
    def insert(self, customer: CustomerEntity):
        ...

    @abstractmethod
    def update(self, customer: CustomerEntity):
        ...

    @abstractmethod
    def delete(self, customer_id):
        ...

    @abstractmethod
    def list(self):
        ...
