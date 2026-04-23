def evaluate_events(events: dict) -> dict:
    """
    Evalúa eventos de riesgo cuando la carga ya salió del puerto.
    """
    route_deviation = events.get("route_deviation", "none")
    gps_lock_status = events.get("gps_lock_status", "secure")
    assault_alert = events.get("assault_alert", False)
    driver_fatigue = events.get("driver_fatigue", "low")

    reasons = []

    if assault_alert:
        reasons.append("Se detectó intento de asalto al camión.")
        reasons.append("Debe emitirse alarma a la comisaría más cercana.")
        return {
            "status": "bloqueada",
            "reasons": reasons
        }

    if gps_lock_status == "tampered":
        reasons.append("Se detectó manipulación o violación del candado GPS.")
        reasons.append("Debe emitirse alarma a la comisaría más cercana.")
        return {
            "status": "bloqueada",
            "reasons": reasons
        }

    if route_deviation == "critical":
        reasons.append("Se detectó desvío crítico de ruta.")
        return {
            "status": "bloqueada",
            "reasons": reasons
        }

    if driver_fatigue == "high":
        reasons.append("Se detectó fatiga alta del conductor.")
        reasons.append("Debe activarse alarma en cabina para detención y cambio de conductor.")
        return {
            "status": "observada",
            "reasons": reasons
        }

    if route_deviation == "moderate":
        reasons.append("Se detectó desvío moderado de ruta.")
        return {
            "status": "observada",
            "reasons": reasons
        }

    if driver_fatigue == "medium":
        reasons.append("Se detectó fatiga media del conductor.")
        return {
            "status": "observada",
            "reasons": reasons
        }

    reasons.append("Trayecto sin eventos críticos reportados.")
    return {
        "status": "habilitada",
        "reasons": reasons
    }