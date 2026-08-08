from fastapi import APIRouter, Depends
from pytest import Session

from database import get_db
from schemas.predict import (
    WinePredictRequest,
    WinePredictResponse,
)
from service.predict_service import predict_wine

router = APIRouter(
    prefix="/predict",
    tags=["predict"]
)
@router.post(
    "",
    response_model=WinePredictResponse
)

def predict(request: WinePredictRequest, db: Session = Depends(get_db)):
    return predict_wine(request,db)