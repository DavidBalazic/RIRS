from fastapi.testclient import TestClient
from app.main import app
from tests.test_db import test_db

client = TestClient(app)

def test_get_letalo(test_db):
    response = client.get("/pridobiLetala/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_letalo(test_db):
    new_letalo = {
        "ime_letala": "string",
        "tip": "string",
        "registrska_st": "string",
        "Polet_idPolet": 0
    }
    response = client.post("/dodajLetalo/", json=new_letalo)
    assert response.status_code == 200
    assert response.json()["ime_letala"] == new_letalo["ime_letala"]

def test_update_nonexistent_letalo(test_db):
    update_data = {
        "ime_letala": "Nonexistent Plane",
        "tip": "Nonexistent Type",
        "registrska_st": "NON123",
        "Polet_idPolet": 1
    }
    response = client.put("/letalo/999", json=update_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Letalo not found"}    
    
def test_update_letalo(test_db):
    update_data = {
        "ime_letala": "Updated Plane",
        "tip": "Boeing 737",
        "registrska_st": "UPD123",
        "Polet_idPolet": None
    }
    response = client.put("/letalo/1", json=update_data)
    if response.status_code == 200:
        assert response.json()["message"] == "Letalo with id 1 updated successfully"
        
def test_read_letalo_existing(test_db):
    new_letalo = {
        "ime_letala": "Boeing 737",
        "tip": "Passenger",
        "registrska_st": "LJ-1234",
        "Polet_idPolet": 1
    }
    create_response = client.post("/dodajLetalo/", json=new_letalo)
    letalo_id = create_response.json()["idLetalo"]
    
    response = client.get(f"/letalo/{letalo_id}")
    data = response.json()
    
    assert response.status_code == 200
    assert data["ime_letala"] == "Boeing 737"
    assert data["tip"] == "Passenger"
    assert data["registrska_st"] == "LJ-1234"
    assert data["Polet_idPolet"] == 1
    
def test_read_letalo_not_found(test_db):
    response = client.get("/letalo/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Letalo not found"
    
def test_read_letalo_invalid_id(test_db):
    response = client.get("/letalo/abc")
    assert response.status_code == 422