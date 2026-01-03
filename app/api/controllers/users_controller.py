from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users import BaseUserManager, IntegerIDMixin
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.models.user import User
from app.schemas.user import UserRead, UserCreate, UserUpdate
from app.core.security import auth_backend
from app.core.config import settings


def get_user_db(db: Session = Depends(get_db)):
    yield SQLAlchemyUserDatabase(db, User)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.secret_key
    verification_token_secret = settings.secret_key

    async def validate_password(self, password: str, user: User | None = None) -> None:
        if len(password) < 6:
            raise ValueError("Password too short")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)
users_router = fastapi_users.get_users_router(UserRead, UserUpdate)

