from app.orchestrator import process_operation


def test_operation_approved():
    data = {
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

    result = process_operation(data)
    assert result["operation_status"] == "APPROVED"
