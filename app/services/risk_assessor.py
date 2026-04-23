from typing import Dict, Any, List


def assess_risk(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calcula un score de riesgo simulado en base a reglas simples.
    """
    observations: List[str] = []
    risk_score = 0

    driver = data.get("driver", {})
    gps = data.get("gps", {})
    incident = data.get("incident_history", {})
    cargo = data.get("cargo", {})

    fatigue_level = driver.get("fatigue_level", "low").lower()
    gps_zone = gps.get("zone", "safe").lower()
    previous_incidents = incident.get("previous_incidents", 0)
    cargo_value = cargo.get("declared_value", 0)

    if fatigue_level == "medium":
        risk_score += 20
        observations.append("Driver fatigue level is medium")
    elif fatigue_level == "high":
        risk_score += 40
        observations.append("Driver fatigue level is high")

    if gps_zone == "warning":
        risk_score += 20
        observations.append("Vehicle is in a warning GPS zone")
    elif gps_zone == "high_risk":
        risk_score += 40
        observations.append("Vehicle is in a high-risk GPS zone")

    if previous_incidents >= 1:
        risk_score += 15
        observations.append("Previous operational incidents detected")

    if previous_incidents >= 3:
        risk_score += 15
        observations.append("High number of previous incidents")

    if cargo_value > 100000:
        risk_score += 20
        observations.append("High-value cargo detected")

    if risk_score >= 70:
        risk_level = "high"
    elif risk_score >= 40:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "observations": observations,
        "details": "Risk assessment completed"
    }