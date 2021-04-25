from fastapi import APIRouter
from .endpoints import addresses, users

api_router = APIRouter()
api_router.include_router(addresses.router, prefix="/addresses", tags=["addresses"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
