from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/prediction"
)

class Prediction(BaseModel):
    id :int
    amount :int
    hour:int
    overseas: str
    result: str
    probability: float

predictions = {}

@router.get("/")
def getAll():
    return predictions

@router.get("/{predictions_id}")
def get(predictions_id:int):
    if predictions_id not in predictions:
        raise HTTPException
    return predictions[predictions_id]

@router.post("/")
def post(pre:Prediction):
    if pre.id in predictions:
        raise HTTPException
    predictions[pre.id] = pre

@router.put("/{predictions_id}")
def put(predictions_id:int, pre:Prediction):
    if predictions_id not in predictions:
        raise HTTPException
    predictions[predictions_id] = pre

@router.delete("/{predictions_id}")
def delete(predictions_id:int):
    if predictions_id not in predictions:
        raise HTTPException
    predictions.pop(predictions_id)
