from abc import ABC, abstractmethod
from typing import Sequence

from customer.domain.entities import Customer as CustomerEntity


class AbstractCustomerRepository(ABC):
    @abstractmethod
    def insert(self, customer: CustomerEntity) -> CustomerEntity | None:
        ...

    @abstractmethod
    def update(self, customer: CustomerEntity) -> CustomerEntity | None:
        ...

    @abstractmethod
    def get_by_id(self, customer_id) -> CustomerEntity | None:
        ...

    @abstractmethod
    def delete(self, customer_id):
        ...

    @abstractmethod
    def list(self) -> Sequence[CustomerEntity] | None:
        ...
