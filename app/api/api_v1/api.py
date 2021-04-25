from fastapi import APIRouter
from .endpoints import addresses, users

api_router = APIRouter()
api_router.include_router(addresses.router, tags=["addresses"])
api_router.include_router(users.router, tags=["users"])
