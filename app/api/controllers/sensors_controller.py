from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.services.sensor_service import SensorService
from app.presenters.sensor_presenter import present_index, present_detail
from app.schemas.sensor import SensorIndexOut, SensorDetailOut


router = APIRouter(prefix="/sensors", tags=["sensors"])


@router.get("/", response_model=list[SensorIndexOut])
def index(db: Session = Depends(get_db)):
    svc = SensorService(db)
    sensors = svc.list_all()
    return present_index(sensors)


@router.get("/{sensor_id}", response_model=SensorDetailOut)
def show(sensor_id: int, db: Session = Depends(get_db)):
    svc = SensorService(db)
    sensor = svc.get_one(sensor_id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return present_detail(sensor)

