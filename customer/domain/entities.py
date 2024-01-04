import re
import uuid

from pydantic import BaseModel, Field, EmailStr, validator
from customer.domain.exceptions import InvalidPhoneNumberException


class Customer(BaseModel):
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
    first_name: str
    last_name: str
    email: EmailStr
    phone: str

    @validator('phone')
    def phone_validator(cls, v):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise InvalidPhoneNumberException("Invalid Phone Number.")
        return v
