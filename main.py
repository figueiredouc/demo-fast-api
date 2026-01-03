from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.core.db import engine, SessionLocal
from app.core.config import settings
from app.api.routes import api_router
from app.admin.admin import mount_admin
from app.models.base import Base
from app.models.user import User
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher


app = FastAPI(title="fastapi-demo")
app.include_router(api_router, prefix="/v1")


# Admin
mount_admin(app, engine)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    # Seed superuser if not exists
    db: Session = SessionLocal()
    try:
        su = db.query(User).filter(User.email == settings.superuser_email).first()
        if not su:
            pwd = PasswordHash([BcryptHasher()])
            su = User(
                email=settings.superuser_email,
                hashed_password=pwd.hash(settings.superuser_password),
                is_active=True,
                is_superuser=True
            )
            db.add(su)
            db.commit()
    finally:
        db.close()

