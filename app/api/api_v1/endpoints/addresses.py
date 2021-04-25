from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import address_crud
from app.schemas.address import Address, AddressCreate

router = APIRouter()


@router.post("", response_model=Address, status_code=201)
def create_address(address_in: AddressCreate, db: Session = Depends(deps.get_db)) -> Any:
    """
    Creates a new address
    :return:
    """
    return address_crud.address.create(db, obj_in=address_in)


@router.get("/{address_id}", response_model=Address)
def get_address_by_id(address_id: int, db: Session = Depends(deps.get_db)) -> Any:
    return address_crud.address.get(db, id=address_id)
