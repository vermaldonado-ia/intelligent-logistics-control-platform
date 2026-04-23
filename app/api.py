from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.orchestrator import process_operation


app = FastAPI(
    title="Intelligent Logistics Control Platform API",
    description=(
    "API para evaluación simulada de operaciones logísticas "
    "y control de acceso"
),
    version="1.0.0"
)


class OperationRequest(BaseModel):
    payload: Dict[str, Any]


@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/evaluate")
def evaluate_operation(request: OperationRequest) -> Dict[str, Any]:
    try:
        result = process_operation(request.payload)
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
