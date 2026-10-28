
from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Performance Prediction" in response.data


def test_prediction():
    client = app.test_client()
    response = client.get("/predict?hours=8")

    assert response.status_code == 200
    assert b"Good performance expected" in response.data


def test_invalid_hours():
    client = app.test_client()
    response = client.get("/predict?hours=30")

    assert response.status_code == 400


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
