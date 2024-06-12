from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "price": 10.5})
    assert response.status_code == 201
    assert response.json() == {"name": "Test Item", "price": 10.5, "id": 1}

def test_read_item():
    item_id = 1
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "price": 10.5, "id": 1}

def test_update_item():
    item_id = 1
    response = client.put(f"/items/{item_id}", json={"name": "Updated Test Item", "price": 12.0})
    assert response.status_code == 200
    assert response.json() == {"name": "Updated Test Item", "price": 12.0, "id": 1}

def test_delete_item():
    item_id = 1
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204

def test_item_not_found():
    item_id = 999
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
