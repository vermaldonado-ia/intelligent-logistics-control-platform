from typing import Dict, Any, List

from app.services.document_validator import validate_documents
from app.services.access_control import evaluate_access
from app.services.risk_assessor import assess_risk
from app.services.ticket_generator import generate_ticket
from app.services.notification_service import send_notification


def process_operation(data: Dict[str, Any]) -> Dict[str, Any]:
    document_result = validate_documents(data)
    access_result = evaluate_access(data)
    risk_result = assess_risk(data)

    all_issues: List[str] = []
    all_observations: List[str] = []

    all_issues.extend(document_result.get("issues", []))
    all_issues.extend(access_result.get("issues", []))
    all_observations.extend(risk_result.get("observations", []))

    if document_result["status"] == "rejected" or access_result["status"] == "rejected":
        final_status = "REJECTED"
    elif risk_result["risk_level"] == "high":
        final_status = "REVIEW_REQUIRED"
    else:
        final_status = "APPROVED"

    summary = {
        "issues": all_issues,
        "observations": all_observations,
        "risk_level": risk_result["risk_level"],
        "risk_score": risk_result["risk_score"],
    }

    ticket = generate_ticket(final_status, summary)
    notification = send_notification(ticket)

    return {
        "operation_status": final_status,
        "document_validation": document_result,
        "access_control": access_result,
        "risk_assessment": risk_result,
        "ticket": ticket,
        "notification": notification,
    }
