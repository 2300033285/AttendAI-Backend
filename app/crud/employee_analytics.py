from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.employee import Employee


def get_employee_analytics(db: Session):

    total_employees = db.query(Employee).count()

    active_employees = (
        db.query(Employee)
        .filter(Employee.status == True)
        .count()
    )

    inactive_employees = (
        db.query(Employee)
        .filter(Employee.status == False)
        .count()
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

    department_count = {
        department: count
        for department, count in department_data
    }

    designation_count = {
        designation: count
        for designation, count in designation_data
    }

    return {
        "total_employees": total_employees,
        "active_employees": active_employees,
        "inactive_employees": inactive_employees,
        "department_count": department_count,
        "designation_count": designation_count,
    }