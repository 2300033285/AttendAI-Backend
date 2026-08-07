from sqlalchemy.orm import Session

from app.crud.attendance import (
    create_attendance,
    get_all_attendance,
    get_attendance_by_id,
    update_attendance,
    delete_attendance,
)

from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
)


def create_attendance_service(db: Session, attendance: AttendanceCreate):
    return create_attendance(db, attendance)


def get_all_attendance_service(db: Session):
    return get_all_attendance(db)


def get_attendance_service(db: Session, attendance_id: int):
    return get_attendance_by_id(db, attendance_id)


def update_attendance_service(
    db: Session,
    attendance_id: int,
    attendance: AttendanceUpdate,
):
    return update_attendance(db, attendance_id, attendance)


def delete_attendance_service(
    db: Session,
    attendance_id: int,
):
    return delete_attendance(db, attendance_id)