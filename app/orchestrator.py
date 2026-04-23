from services.document_validator import validate_documents
from services.access_validator import validate_access
from services.event_evaluator import evaluate_events
from services.notification_service import (
    build_phone_notification,
    save_notification_to_file,
)
from services.ticket_generator import (
    build_access_ticket,
    save_ticket_to_file,
)


def consolidate_status(document_result: dict, access_result: dict, event_result: dict) -> str:
    """
    Consolida el estado final de la operación.
    """
    results = [document_result, access_result, event_result]

    if any(result["status"] == "bloqueada" for result in results):
        return "bloqueada"

    if any(result["status"] == "observada" for result in results):
        return "observada"

    return "habilitada"


def process_operation(input_data: dict) -> dict:
    """
    Orquesta el flujo completo del MVP.
    """
    document_result = validate_documents(input_data.get("documents", {}))

    access_result = validate_access(
        input_data.get("access", {}),
        input_data.get("driver", {}),
        input_data.get("vehicle", {}),
        input_data.get("shipment", {})
    )

    event_result = evaluate_events(input_data.get("events", {}))

    final_status = consolidate_status(document_result, access_result, event_result)

    notification_result = {
        "status": "not_generated",
        "phone": None,
        "message": None
    }

    ticket_result = {
        "status": "not_generated",
        "ticket": None
    }

    if access_result["status"] == "habilitada":
        notification_result = build_phone_notification(
            driver=input_data.get("driver", {}),
            vehicle=input_data.get("vehicle", {}),
            shipment=input_data.get("shipment", {}),
            access=input_data.get("access", {})
        )
        save_notification_to_file(notification_result, "../output/phone_notification.txt")

        ticket_result = build_access_ticket(
            driver=input_data.get("driver", {}),
            vehicle=input_data.get("vehicle", {}),
            shipment=input_data.get("shipment", {}),
            access=input_data.get("access", {}),
            access_status=access_result["status"],
            observations=access_result.get("reasons", [])
        )
        save_ticket_to_file(ticket_result["ticket"], "../output/access_ticket.txt")

    return {
        "document_validation": document_result,
        "access_validation": access_result,
        "event_evaluation": event_result,
        "final_status": final_status,
        "phone_notification": notification_result,
        "access_ticket": ticket_result
    }