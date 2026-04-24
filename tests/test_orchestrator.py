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


def test_operation_review_required_high_risk():
    data = {
        "driver": {"authorized": True, "fatigue_level": "high"},
        "vehicle": {"authorized": True},
        "cargo": {"type": "container", "declared_value": 200000},
        "port_access_allowed": True,
        "gps": {"zone": "high_risk"},
        "incident_history": {"previous_incidents": 3},
        "documents": {
            "driver_license": {"present": True, "expiry_date": "2027-12-31"},
            "vehicle_permit": {"present": True, "expiry_date": "2027-12-31"},
            "cargo_manifest": {"present": True, "expiry_date": "2027-12-31"},
        },
    }

    result = process_operation(data)
    assert result["operation_status"] == "REVIEW_REQUIRED"


def test_operation_rejected_unauthorized_driver():
    data = {
        "driver": {"authorized": False, "fatigue_level": "low"},
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
    assert result["operation_status"] == "REJECTED"


def test_operation_rejected_expired_documents():
    data = {
        "driver": {"authorized": True, "fatigue_level": "low"},
        "vehicle": {"authorized": True},
        "cargo": {"type": "container", "declared_value": 1000},
        "port_access_allowed": True,
        "gps": {"zone": "safe"},
        "incident_history": {"previous_incidents": 0},
        "documents": {
            "driver_license": {"present": True, "expiry_date": "2020-01-01"},
            "vehicle_permit": {"present": True, "expiry_date": "2027-12-31"},
            "cargo_manifest": {"present": True, "expiry_date": "2027-12-31"},
        },
    }

    result = process_operation(data)
    assert result["operation_status"] == "REJECTED"
