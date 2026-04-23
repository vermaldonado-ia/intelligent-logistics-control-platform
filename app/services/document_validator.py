def validate_documents(documents: dict) -> dict:
    """
    Valida el estado documental previo al arribo al puerto.
    """
    document_status = documents.get("status", "rejected")
    days_to_deadline = documents.get("days_to_deadline", 0)
    deadline_expired = documents.get("deadline_expired", False)
    customs_agency_response_required = documents.get(
        "customs_agency_response_required",
        False
    )

    reasons = []

    if document_status == "approved":
        reasons.append("Documentación aprobada correctamente por el ente fiscalizador.")
        return {
            "status": "habilitada",
            "reasons": reasons
        }

    if document_status == "observed":
        if deadline_expired:
            reasons.append("Documentación observada con plazo vencido para regularización.")
            reasons.append("Existe riesgo de eliminación o bloqueo de la mercancía.")
            return {
                "status": "bloqueada",
                "reasons": reasons
            }

        reasons.append("Documentación observada.")
        reasons.append(
            f"La agencia de aduana debe regularizar la información dentro de {days_to_deadline} día(s)."
        )
        if customs_agency_response_required:
            reasons.append("Se requiere acción de la agencia de aduana.")
        return {
            "status": "observada",
            "reasons": reasons
        }

    if document_status == "rejected":
        if deadline_expired:
            reasons.append("Documentación rechazada con plazo vencido.")
            reasons.append("La mercancía queda en riesgo de eliminación.")
            return {
                "status": "bloqueada",
                "reasons": reasons
            }

        reasons.append("Documentación rechazada.")
        reasons.append(
            f"La agencia de aduana debe volver a ingresar la documentación dentro de {days_to_deadline} día(s)."
        )
        if customs_agency_response_required:
            reasons.append("Se requiere acción inmediata de la agencia de aduana.")
        return {
            "status": "observada",
            "reasons": reasons
        }

    reasons.append("Estado documental no reconocido.")
    return {
        "status": "bloqueada",
        "reasons": reasons
    }