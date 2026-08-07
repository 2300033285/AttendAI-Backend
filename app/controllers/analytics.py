from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.security import get_current_user
from app.schemas.analytics import AnalyticsResponse
from app.services.analytics_service import analytics_service

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/",
    response_model=AnalyticsResponse,
    summary="Attendance Analytics",
)
def analytics(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return analytics_service(db)