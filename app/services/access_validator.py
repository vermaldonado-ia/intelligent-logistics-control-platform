def validate_access(access: dict, driver: dict, vehicle: dict, shipment: dict) -> dict:
    """
    Valida si el camión puede ingresar al puerto.
    """
    scheduled_date = access.get("scheduled_date", "")
    scheduled_time = access.get("scheduled_time", "")
    gate_number = access.get("gate_number", "")
    data_complete = access.get("data_complete", False)
    data_valid = access.get("data_valid", False)

    driver_name = driver.get("full_name", "")
    driver_rut = driver.get("rut", "")
    license_plate = vehicle.get("license_plate", "")
    shipment_number = shipment.get("shipment_number", "")

    reasons = []

    required_fields_present = all([
        scheduled_date,
        scheduled_time,
        gate_number,
        driver_name,
        driver_rut,
        license_plate,
        shipment_number
    ])

    if not required_fields_present or not data_complete:
        reasons.append("Datos de acceso incompletos.")
        reasons.append("Debe esperar validación y rectificación por parte de la agencia de aduana.")
        return {
            "status": "observada",
            "reasons": reasons
        }

    if not data_valid:
        reasons.append("Datos de acceso inválidos.")
        reasons.append("El camión no puede ingresar al puerto.")
        return {
            "status": "bloqueada",
            "reasons": reasons
        }

    reasons.append("Datos completos y validados. Acceso autorizado al puerto.")
    return {
        "status": "habilitada",
        "reasons": reasons
    }