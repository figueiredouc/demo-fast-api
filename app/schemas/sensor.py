from pydantic import BaseModel


class SensorIndexOut(BaseModel):
    id: int
    name: str
    kind: str
    is_active: bool


class SensorDetailOut(SensorIndexOut):
    location: str

