from fastapi import APIRouter
from app.api.controllers import sensors_controller
from app.api.controllers import users_controller


api_router = APIRouter()
api_router.include_router(users_controller.auth_router, prefix="/auth/jwt")
api_router.include_router(users_controller.register_router, prefix="/auth")
api_router.include_router(sensors_controller.router)

