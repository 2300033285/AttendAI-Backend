from sqlalchemy.orm import Session
from sqlalchemy import extract
from app.models.attendance import Attendance


def daily_report(db: Session, report_date):
    return db.query(Attendance).filter(
        Attendance.date == report_date
    ).all()


def monthly_report(db: Session, month: int):
    return db.query(Attendance).filter(
        extract("month", Attendance.date) == month
    ).all()


def user_report(db: Session, user_id: int):
    return db.query(Attendance).filter(
        Attendance.user_id == user_id
    ).all()