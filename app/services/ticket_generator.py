from datetime import datetime
from typing import Dict, Any
from uuid import uuid4


def generate_ticket(final_status: str, evaluation_summary: Dict[str, Any]) -> Dict[str, Any]:
    """
    Genera un ticket operacional con trazabilidad básica.
    """
    ticket_id = f"TICKET-{uuid4().hex[:8].upper()}"
    issued_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    qr_simulated = f"QR::{ticket_id}::{final_status}"

    return {
        "ticket_id": ticket_id,
        "issued_at": issued_at,
        "status": final_status,
        "observations": evaluation_summary.get("observations", []),
        "issues": evaluation_summary.get("issues", []),
        "risk_level": evaluation_summary.get("risk_level", "unknown"),
        "risk_score": evaluation_summary.get("risk_score", 0),
        "qr_code": qr_simulated
    }