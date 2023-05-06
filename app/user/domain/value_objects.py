from dataclasses import dataclass

from app.__seedwork.domain.value_objects import ValueObject


@dataclass(frozen=True)
class Address(ValueObject):
    country: str
    street: str
    zip_code: str
