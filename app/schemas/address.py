from pydantic import BaseModel


class AddressBase(BaseModel):
    place: str


class AddressCreate(AddressBase):
    """
    Can add extra fields here needed on Address creation
    """
    pass


class AddressUpdate(AddressBase):
    """
    Can add extra fields here needed on Address update
    """
    pass


class AddressInDBBase(AddressBase):
    id: int

    class Config:
        orm_mode = True


class Address(AddressInDBBase):
    """
    Fields to be returned from the endpoints
    """
    pass
