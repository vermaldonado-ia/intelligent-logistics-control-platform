from datetime import datetime
from typing import Any, Dict, List

REQUIRED_DOCUMENTS = [
    "driver_license",
    "vehicle_permit",
    "cargo_manifest",
]


def _parse_date(date_str: str) -> datetime | None:
    """
    Convierte una fecha en formato YYYY-MM-DD a datetime.
    Retorna None si el formato es inválido.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except (ValueError, TypeError):
        return None


def validate_documents(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Valida que existan los documentos requeridos y que no estén vencidos.
    """
    documents = data.get("documents", {})
    issues: List[str] = []

    for doc_name in REQUIRED_DOCUMENTS:
        if doc_name not in documents:
            issues.append(f"Missing required document: {doc_name}")
            continue

        doc_info = documents[doc_name]

        if not isinstance(doc_info, dict):
            issues.append(f"Invalid document format: {doc_name}")
            continue

        is_present = doc_info.get("present", False)

        if not is_present:
            issues.append(f"Document not present: {doc_name}")
            continue

        expiry_date = doc_info.get("expiry_date")
        parsed_expiry = _parse_date(expiry_date)

        if parsed_expiry is None:
            issues.append(f"Invalid expiry date format for: {doc_name}")
            continue

        if parsed_expiry.date() < datetime.now().date():
            issues.append(f"Expired document: {doc_name}")

    status = "approved" if not issues else "rejected"

    return {
        "status": status,
        "issues": issues,
        "details": "Document validation completed",
    }
