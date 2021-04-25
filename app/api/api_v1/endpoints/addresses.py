from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.post("")
def create_address() -> Any:
    """
    Creates a new address
    :return:
    """
    pass
