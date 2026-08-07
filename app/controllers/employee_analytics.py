from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.security import get_current_user

from app.schemas.employee_analytics import EmployeeAnalyticsResponse
from app.services.employee_analytics_service import employee_analytics_service

router = APIRouter(
    prefix="/employee-analytics",
    tags=["Employee Analytics"],
)


@router.get(
    "/",
    response_model=EmployeeAnalyticsResponse,
    summary="Employee Analytics",
)
def get_employee_analytics_api(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return employee_analytics_service(db)