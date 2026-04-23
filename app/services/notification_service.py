from typing import Dict, Any


def send_notification(ticket: Dict[str, Any]) -> Dict[str, Any]:
    """
    Simula el envío de una notificación operacional.
    """
    message = (
        f"Notification sent | Ticket: {ticket['ticket_id']} | "
        f"Status: {ticket['status']} | Risk: {ticket['risk_level']}"
    )

    return {
        "notification_status": "sent",
        "message": message
    }
    
