from sqladmin import Admin, ModelView
from fastapi import FastAPI
from sqlalchemy import Engine
from app.models.sensor import Sensor
from app.models.user import User


class SensorAdmin(ModelView, model=Sensor):
    column_list = [Sensor.id, Sensor.name, Sensor.kind, Sensor.location, Sensor.is_active]


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.is_active, User.is_superuser]


def mount_admin(app: FastAPI, engine: Engine):
    admin = Admin(app, engine)
    admin.add_view(SensorAdmin)
    admin.add_view(UserAdmin)
    return admin

