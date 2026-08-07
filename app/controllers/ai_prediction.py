from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.security import get_current_user

from app.schemas.ai_prediction import AIPredictionResponse
from app.services.ai_prediction_service import ai_prediction_service

router = APIRouter(
    prefix="/ai-prediction",
    tags=["AI Prediction"],
)


@router.get(
    "/",
    response_model=AIPredictionResponse,
    summary="AI Attendance Prediction",
)
def get_ai_prediction_api(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return ai_prediction_service(db)