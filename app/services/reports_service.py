from sqlalchemy.orm import Session

from app.crud.reports import (
    daily_report,
    monthly_report,
    user_report,
)


def get_daily_report(db: Session, report_date):
    return daily_report(db, report_date)


def get_monthly_report(db: Session, month: int):
    return monthly_report(db, month)


def get_user_report(db: Session, user_id: int):
    return user_report(db, user_id)