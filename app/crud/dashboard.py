from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.attendance import Attendance


def get_dashboard_stats(db: Session):

    total_employees = db.query(Employee).count()

    active_employees = (
        db.query(Employee)
        .filter(Employee.status.is_(True))
        .count()
    )

    total_attendance = db.query(Attendance).count()

    present = (
        db.query(Attendance)
        .filter(Attendance.status == "Present")
        .count()
    )

    absent = (
        db.query(Attendance)
        .filter(Attendance.status == "Absent")
        .count()
    )

    late = (
        db.query(Attendance)
        .filter(Attendance.status == "Late")
        .count()
    )

    return {
        "total_employees": total_employees,
        "active_employees": active_employees,
        "total_attendance": total_attendance,
        "present": present,
        "absent": absent,
        "late": late,
    }