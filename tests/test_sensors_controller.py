import pytest
from httpx import Client
from sqlalchemy.orm import Session
from app.core.db import SessionLocal, engine
from app.models.base import Base
from app.models.sensor import Sensor
from main import app


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client():
    with Client(app=app, base_url="http://test") as c:
        yield c


def test_index_returns_empty_list(client):
    res = client.get("/v1/sensors/")
    assert res.status_code == 200
    assert res.json() == []


def test_index_returns_items(client, db):
    db.add_all([
        Sensor(name="Temp-01", kind="temperature", location="Lab", is_active=True),
        Sensor(name="Hum-01", kind="humidity", location="Hall", is_active=False),
    ])
    db.commit()
    res = client.get("/v1/sensors/")
    assert res.status_code == 200
    assert len(res.json()) == 2


def test_show_returns_one(client, db):
    s = Sensor(name="Temp-02", kind="temperature", location="Roof", is_active=True)
    db.add(s)
    db.commit()
    db.refresh(s)
    res = client.get(f"/v1/sensors/{s.id}")
    assert res.status_code == 200
    body = res.json()
    assert body["id"] == s.id
    assert body["location"] == "Roof"


def test_show_404(client):
    res = client.get("/v1/sensors/9999")
    assert res.status_code == 404

