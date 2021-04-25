from app.crud.base import CRUDBase
from app.models import Address
from app.schemas.address import AddressCreate, AddressUpdate


class CRUDAddress(CRUDBase[Address, AddressCreate, AddressUpdate]):
    pass


address = CRUDAddress(Address)
