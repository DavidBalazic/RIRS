from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime
from tests.test_db import test_db
from app.models.models import PoletModel

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
    
def test_delete_invalid_input(test_db):
    polet_id = "abc" 
    response = client.delete(f"/polet/{polet_id}")
    assert response.status_code == 422
    
# GET pridobiPoletePilota
def test_get_poleti_for_pilot_valid(test_db):
    polet1 = PoletModel(cas_vzleta="20/12/2024 14:00", cas_pristanka="20/12/2024 16:00", Pilot_idPilot=10)
    polet2 = PoletModel(cas_vzleta="21/12/2024 10:00", cas_pristanka="21/12/2024 12:00", Pilot_idPilot=10)
    test_db.add_all([polet1, polet2])
    test_db.commit()
    
    response = client.get("/pridobiPoletePilota/10")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["Pilot_idPilot"] == 10
    assert data[1]["Pilot_idPilot"] == 10
    
def test_get_poleti_for_pilot_invalid_pilot_id(test_db):
    response = client.get("/pridobiPoletePilota/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "No flights found for pilot with ID 999"
    
def test_get_poleti_for_pilot_invalid_input(test_db):
    response = client.get("/pridobiPoletePilota/abc") 

    assert response.status_code == 422
    
def test_get_poleti_for_pilot_empty_db(test_db):
    test_db.query(PoletModel).delete()
    test_db.commit()

    response = client.get("/pridobiPoletePilota/1")

    assert response.status_code == 404
    assert response.json()["detail"] == "No flights found for pilot with ID 1"