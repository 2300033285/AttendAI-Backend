from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.security import get_current_user

from app.schemas.insights import InsightsResponse
from app.services.insights_service import insights_service

router = APIRouter(
    prefix="/insights",
    tags=["Insights"],
)


@router.get(
    "/",
    response_model=InsightsResponse,
    summary="Insights",
)
def get_insights_api(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return insights_service(db)