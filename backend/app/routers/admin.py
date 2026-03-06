from fastapi import APIRouter, Query
from app.models.schemas import VectorizeResponse
from app.services.vector_service import vectorize_schemes

router = APIRouter()


@router.post("/admin/vectorize", response_model=VectorizeResponse)
async def vectorize(force: bool = Query(False, description="Force re-vectorization")):
    result = vectorize_schemes(force=force)
    return VectorizeResponse(**result)
