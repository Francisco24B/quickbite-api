
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders/", json={"item": "Pizza"})
    assert response.status_code == 200
    assert response.json()["order"]["item"] == "Pizza"
