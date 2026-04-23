from typing import Dict, Any, List


ALLOWED_CARGO_TYPES = [
    "general",
    "container",
    "fragile",
    "hazardous",
]


def evaluate_access(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evalúa si el conductor, vehículo y carga cumplen condiciones de acceso.
    """
    issues: List[str] = []

    driver = data.get("driver", {})
    vehicle = data.get("vehicle", {})
    cargo = data.get("cargo", {})

    driver_authorized = driver.get("authorized", False)
    vehicle_authorized = vehicle.get("authorized", False)
    cargo_type = cargo.get("type", "").lower()
    port_access_allowed = data.get("port_access_allowed", False)

    if not driver_authorized:
        issues.append("Driver is not authorized")

    if not vehicle_authorized:
        issues.append("Vehicle is not authorized")

    if cargo_type not in ALLOWED_CARGO_TYPES:
        issues.append(f"Cargo type is not allowed: {cargo_type}")

    if not port_access_allowed:
        issues.append("Port access is not allowed")

    status = "approved" if not issues else "rejected"

    return {
        "status": status,
        "issues": issues,
        "details": "Access control evaluation completed"
    }
    
