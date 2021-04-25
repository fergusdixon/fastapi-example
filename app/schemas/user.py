from typing import List

from pydantic import BaseModel

from app.schemas.address import Address


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    """Can add extra fields here needed on user creation."""


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):

    """Fields to be returned from the endpoints."""


class UserWithAddresses(User):

    """Fields to be returned from the endpoints with linked addresses."""

    addresses: List[Address]
