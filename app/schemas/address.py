from typing import List

from pydantic import BaseModel


class AddressBase(BaseModel):
    place: str


class AddressCreate(AddressBase):
    """Can add extra fields here needed on Address creation."""


class AddressInDBBase(AddressBase):
    id: int

    class Config:
        orm_mode = True


class Address(AddressInDBBase):
    """Fields to be returned from the endpoints."""


class AddressWithUsers(Address):
    """Fields to be returned from the endpoints including users."""

    from app.schemas.user import User

    users: List[User]
