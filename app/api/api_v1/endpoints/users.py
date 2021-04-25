from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import user_crud
from app.schemas.user import UserCreate, User

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
