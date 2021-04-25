from typing import List

from pydantic import BaseModel

from app.schemas.address import Address


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    """
    Can add extra fields here needed on user creation
    """
    pass


class UserUpdate(UserBase):
    """
    Can add extra fields here needed on user update
    """
    pass


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    """
    Fields to be returned from the endpoints
    """
    addresses: List[Address]
