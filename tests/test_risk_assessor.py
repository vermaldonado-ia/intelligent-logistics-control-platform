from app.services.risk_assessor import assess_risk


def test_low_risk():
    data = {
        "driver": {"fatigue_level": "low"},
        "gps": {"zone": "safe"},
        "incident_history": {"previous_incidents": 0},
        "cargo": {"declared_value": 1000},
    }

    result = assess_risk(data)
    assert result["risk_level"] == "low"


def test_high_risk():
    data = {
        "driver": {"fatigue_level": "high"},
        "gps": {"zone": "high_risk"},
        "incident_history": {"previous_incidents": 3},
        "cargo": {"declared_value": 200000},
    }

    result = assess_risk(data)
    assert result["risk_level"] == "high"