from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.security import get_current_user

from app.schemas.anomaly import AnomalyResponse
from app.services.anomaly_service import anomaly_service

router = APIRouter(
    prefix="/anomalies",
    tags=["Anomaly Detection"],
)


@router.get(
    "/",
    response_model=AnomalyResponse,
    summary="Anomaly Detection",
)
def get_anomalies_api(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return anomaly_service(db)