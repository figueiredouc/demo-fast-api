from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.sensor import Sensor


class SensorRepository:
    def __init__(self, db: Session):
        self.db = db

    def all(self) -> list[Sensor]:
        return list(self.db.execute(select(Sensor)).scalars().all())

    def get(self, sensor_id: int) -> Sensor | None:
        return self.db.get(Sensor, sensor_id)

