from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.post("")
def create_user() -> Any:
    """
    Creates a new user
    :return:
    """
    pass
