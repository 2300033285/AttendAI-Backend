from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.security import get_current_user
from app.schemas.attendance import AttendanceResponse
from app.services.reports_service import (
    get_daily_report,
    get_monthly_report,
    get_user_report,
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get(
    "/daily/{report_date}",
    response_model=list[AttendanceResponse],
)
def daily(
    report_date: date,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_daily_report(db, report_date)


@router.get(
    "/monthly/{month}",
    response_model=list[AttendanceResponse],
)
def monthly(
    month: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_monthly_report(db, month)


@router.get(
    "/user/{user_id}",
    response_model=list[AttendanceResponse],
)
def user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_user_report(db, user_id)