from sqlalchemy.orm import Session
from app.repositories.sensor_repository import SensorRepository


class SensorService:
    def __init__(self, db: Session):
        self.repo = SensorRepository(db)

    def list_all(self):
        return self.repo.all()

    def get_one(self, sensor_id: int):
        return self.repo.get(sensor_id)

