from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.employee import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee,
)
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


def create_employee_service(db: Session, employee: EmployeeCreate):
    return create_employee(db, employee)


def get_all_employees_service(db: Session):
    return get_all_employees(db)


def get_employee_service(db: Session, employee_id: int):
    employee = get_employee_by_id(db, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


def update_employee_service(
    db: Session,
    employee_id: int,
    employee: EmployeeUpdate,
):
    updated_employee = update_employee(db, employee_id, employee)

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee


def delete_employee_service(db: Session, employee_id: int):
    deleted_employee = delete_employee(db, employee_id)

    if deleted_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return deleted_employee