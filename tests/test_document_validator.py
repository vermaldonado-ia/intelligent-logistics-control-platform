from app.services.document_validator import validate_documents


def test_documents_valid():
    data = {
        "documents": {
            "driver_license": {"present": True, "expiry_date": "2027-12-31"},
            "vehicle_permit": {"present": True, "expiry_date": "2027-12-31"},
            "cargo_manifest": {"present": True, "expiry_date": "2027-12-31"},
        }
    }

    result = validate_documents(data)
    assert result["status"] == "approved"


def test_documents_missing():
    data = {"documents": {}}

    result = validate_documents(data)
    assert result["status"] == "rejected"
    assert len(result["issues"]) > 0