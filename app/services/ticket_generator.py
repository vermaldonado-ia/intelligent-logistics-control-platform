from datetime import datetime
import uuid


def build_access_ticket(
    driver: dict,
    vehicle: dict,
    shipment: dict,
    access: dict,
    access_status: str,
    observations: list
) -> dict:
    """
    Genera un ticket digital de acceso con metadatos operacionales.
    """
    issue_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticket_code = f"TCK-{uuid.uuid4().hex[:8].upper()}"

    ticket_data = {
        "ticket_code": ticket_code,
        "issue_datetime": issue_datetime,
        "full_name": driver.get("full_name", "No informado"),
        "rut": driver.get("rut", "No informado"),
        "license_plate": vehicle.get("license_plate", "No informado"),
        "shipment_number": shipment.get("shipment_number", "No informado"),
        "gate_number": access.get("gate_number", "No informada"),
        "access_status": access_status,
        "observations": observations,
        "qr_code": f"QR-SIMULATED::{ticket_code}"
    }

    return {
        "status": "generated",
        "ticket": ticket_data
    }


def save_ticket_to_file(ticket_data: dict, file_path: str) -> None:
    """
    Guarda el ticket digital en archivo de texto.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("=== TICKET DIGITAL DE ACCESO ===\n")
        file.write(f"Código ticket   : {ticket_data['ticket_code']}\n")
        file.write(f"Fecha emisión   : {ticket_data['issue_datetime']}\n")
        file.write(f"Conductor       : {ticket_data['full_name']}\n")
        file.write(f"RUT             : {ticket_data['rut']}\n")
        file.write(f"Patente         : {ticket_data['license_plate']}\n")
        file.write(f"Embarque        : {ticket_data['shipment_number']}\n")
        file.write(f"Puerta carga    : {ticket_data['gate_number']}\n")
        file.write(f"Estado acceso   : {ticket_data['access_status']}\n")
        file.write(f"QR simulado     : {ticket_data['qr_code']}\n")

        if ticket_data["observations"]:
            file.write("Observaciones   :\n")
            for item in ticket_data["observations"]:
                file.write(f" - {item}\n")