from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate, AttendanceUpdate


# Create Attendance
def create_attendance(db: Session, attendance: AttendanceCreate):
    new_attendance = Attendance(
        user_id=attendance.user_id,
        date=attendance.date,
        check_in=attendance.check_in,
        check_out=attendance.check_out,
        status=attendance.status,
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance


# Get All Attendance
def get_all_attendance(db: Session):
    return db.query(Attendance).all()


# Get Attendance By ID
def get_attendance_by_id(db: Session, attendance_id: int):
    return db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()


# Update Attendance
def update_attendance(db: Session, attendance_id: int, attendance: AttendanceUpdate):
    db_attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not db_attendance:
        return None

    update_data = attendance.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_attendance, key, value)

    db.commit()
    db.refresh(db_attendance)

    return db_attendance


# Delete Attendance
def delete_attendance(db: Session, attendance_id: int):
    db_attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not db_attendance:
        return None

    db.delete(db_attendance)
    db.commit()

    return db_attendance