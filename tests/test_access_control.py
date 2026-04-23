from app.services.access_control import evaluate_access


def test_access_ok():
    data = {
        "driver": {"authorized": True},
        "vehicle": {"authorized": True},
        "cargo": {"type": "container"},
        "port_access_allowed": True,
    }

    result = evaluate_access(data)
    assert result["status"] == "approved"


def test_access_denied():
    data = {
        "driver": {"authorized": False},
        "vehicle": {"authorized": False},
        "cargo": {"type": "unknown"},
        "port_access_allowed": False,
    }

    result = evaluate_access(data)
    assert result["status"] == "rejected"