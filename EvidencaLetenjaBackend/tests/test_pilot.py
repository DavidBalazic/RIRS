from fastapi.testclient import TestClient
from app.main import app
from tests.test_db import test_db

client = TestClient(app)

def test_get_pilots(test_db):
    response = client.get("/pridobiPilote/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_delete_pilot(test_db):
    # Create a pilot first
    create_response = client.post(
        "/dodajPilota/",
        json={
            "ime": "Eva",
            "priimek": "Zajec"
        },
    )
    assert create_response.status_code == 200
    pilot_id = create_response.json()["idPilot"]

    # Delete the pilot
    delete_response = client.delete(f"/pilot/{pilot_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": f"Pilot deleted successfully"}