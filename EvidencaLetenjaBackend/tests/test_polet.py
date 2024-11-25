from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime
from tests.test_db import test_db

client = TestClient(app)

def test_get_poleti(test_db):
    response = client.get("/pridobiPolete/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_inccorect_dateformat_post_polet(test_db):
    now = datetime.now() 
    new_polet = {
        "cas_vzleta": now.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "cas_pristanka": now.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "Pilot_idPilot": 1
    }
    response = client.post("/dodajPolet/", json=new_polet)
    assert response.status_code == 400
    
def test_post_polet(test_db):
    now = datetime.now() 
    new_polet = {
        "cas_vzleta": now.strftime("%d/%m/%Y %H:%M"),
        "cas_pristanka": now.strftime("%d/%m/%Y %H:%M"),
        "Pilot_idPilot": 1
    }
    response = client.post("/dodajPolet/", json=new_polet)
    assert response.status_code == 200
    
def test_delete_non_existing_polet(test_db):
    polet_id = 9999 
    response = client.delete(f"/polet/{polet_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"Polet not found"