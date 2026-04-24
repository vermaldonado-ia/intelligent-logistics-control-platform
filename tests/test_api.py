from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_evaluate_operation():
    payload = {
        "payload": {
            "driver": {"authorized": True, "fatigue_level": "low"},
            "vehicle": {"authorized": True},
            "cargo": {"type": "container", "declared_value": 1000},
            "port_access_allowed": True,
            "gps": {"zone": "safe"},
            "incident_history": {"previous_incidents": 0},
            "documents": {
                "driver_license": {"present": True, "expiry_date": "2027-12-31"},
                "vehicle_permit": {"present": True, "expiry_date": "2027-12-31"},
                "cargo_manifest": {"present": True, "expiry_date": "2027-12-31"},
            },
        }
    }

    response = client.post("/evaluate", json=payload)
    assert response.status_code == 200
    assert response.json()["operation_status"] == "APPROVED"
    