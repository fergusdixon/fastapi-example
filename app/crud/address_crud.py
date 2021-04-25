from app.crud.base import CRUDBase
from app.models import Address
from app.schemas.address import AddressCreate


class CRUDAddress(CRUDBase[Address, AddressCreate]):
    pass


address = CRUDAddress(Address)
