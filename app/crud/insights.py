from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.employee import Employee
from app.models.attendance import Attendance


def get_insights(db: Session):

    total_employees = db.query(Employee).count()

    active_employees = (
        db.query(Employee)
        .filter(Employee.status == True)
        .count()
    )

    total_attendance = db.query(Attendance).count()

    present_attendance = (
        db.query(Attendance)
        .filter(func.lower(Attendance.status) == "present")
        .count()
    )

    attendance_percentage = 0

    if total_attendance > 0:
        attendance_percentage = round(
            (present_attendance / total_attendance) * 100,
            2
        )

    department_data = (
        db.query(
            Employee.department,
            func.count(Employee.id)
        )
        .group_by(Employee.department)
        .all()
    )

    designation_data = (
        db.query(
            Employee.designation,
            func.count(Employee.id)
        )
        .group_by(Employee.designation)
        .all()
    )

    department_summary = {
        dept: count
        for dept, count in department_data
    }

    designation_summary = {
        designation: count
        for designation, count in designation_data
    }

    return {
        "total_employees": total_employees,
        "active_employees": active_employees,
        "attendance_percentage": attendance_percentage,
        "department_summary": department_summary,
        "designation_summary": designation_summary
    }