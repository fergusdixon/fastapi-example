from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import address_crud, user_crud
from app.schemas.user import User, UserCreate

router = APIRouter()


@router.post("", response_model=User, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(deps.get_db)) -> Any:
    """
    Creates a new user
    :return:
    """
    return user_crud.user.create(db, obj_in=user_in)


@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int, db: Session = Depends(deps.get_db)) -> Any:
    return user_crud.user.get(db, id=user_id)


@router.put("/{user_id}/address/{address_id}")
def assign_address_to_user(user_id: int, address_id: int, db: Session = Depends(deps.get_db)) -> Any:
    user_model = user_crud.user.get(db, id=user_id)
    if not user_model:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found.")

    address_model = address_crud.address.get(db, id=address_id)
    if not address_model:
        raise HTTPException(status_code=404, detail=f"Address {address_id} not found.")

    user_model.addresses.append(address_model)
    db.add(user_model)
    db.commit()
    return True
