from fastapi import APIRouter, HTTPException
from app.schemas.models import CodeRequest, SQLRequest, DocumentRequest, IntelligenceResponse
from app.services.intelligence import IntelligenceService

router = APIRouter(prefix="/api/v1")
service = IntelligenceService()

@router.post("/explain", response_model=IntelligenceResponse)
def explain(request: CodeRequest):
    try:
        return {"result": service.explain(request.language, request.code), "mode": service.mode}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@router.post("/sql", response_model=IntelligenceResponse)
def sql(request: SQLRequest):
    try:
        return {"result": service.generate_sql(request.request, request.schema_context), "mode": service.mode}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@router.post("/document", response_model=IntelligenceResponse)
def document(request: DocumentRequest):
    try:
        return {"result": service.document(request.language, request.code), "mode": service.mode}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
