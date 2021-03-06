from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import address_crud
from app.schemas.address import Address, AddressCreate, AddressWithUsers

router = APIRouter()


@router.post("", response_model=Address, status_code=201)
def create_address(address_in: AddressCreate, db: Session = Depends(deps.get_db)) -> Any:
    """
    Creates a new address
    :return:
    """
    return address_crud.address.create(db, obj_in=address_in)


@router.get("/{address_id}", response_model=AddressWithUsers)
def get_address_by_id(address_id: int, db: Session = Depends(deps.get_db)) -> Any:
    address = address_crud.address.get(db, id=address_id)
    if not address:
        raise HTTPException(status_code=404, detail=f"Address {address_id} not found.")
    return address
