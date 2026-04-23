def build_phone_notification(driver: dict, vehicle: dict, shipment: dict, access: dict) -> dict:
    """
    Construye la notificación telefónica de autorización de ingreso.
    """
    full_name = driver.get("full_name", "No informado")
    rut = driver.get("rut", "No informado")
    phone = driver.get("phone", "No informado")
    license_plate = vehicle.get("license_plate", "No informado")
    shipment_number = shipment.get("shipment_number", "No informado")
    gate_number = access.get("gate_number", "No informada")
    scheduled_date = access.get("scheduled_date", "No informada")
    scheduled_time = access.get("scheduled_time", "No informada")

    message = (
        f"Autorización de ingreso al puerto\n"
        f"Conductor: {full_name}\n"
        f"RUT: {rut}\n"
        f"Patente: {license_plate}\n"
        f"Embarque: {shipment_number}\n"
        f"Puerta de carga: {gate_number}\n"
        f"Fecha ingreso: {scheduled_date}\n"
        f"Hora ingreso: {scheduled_time}\n"
    )

    return {
        "status": "generated",
        "phone": phone,
        "message": message
    }


def save_notification_to_file(notification: dict, file_path: str) -> None:
    """
    Guarda la notificación en archivo de texto.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("=== NOTIFICACIÓN TELEFÓNICA ===\n\n")
        file.write(notification["message"])