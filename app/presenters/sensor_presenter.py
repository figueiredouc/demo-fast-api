from typing import Iterable
from app.models.sensor import Sensor
from app.schemas.sensor import SensorIndexOut, SensorDetailOut


def present_index(items: Iterable[Sensor]) -> list[SensorIndexOut]:
    return [SensorIndexOut(id=s.id, name=s.name, kind=s.kind, is_active=s.is_active) for s in items]


def present_detail(s: Sensor) -> SensorDetailOut:
    return SensorDetailOut(id=s.id, name=s.name, kind=s.kind, is_active=s.is_active, location=s.location)

