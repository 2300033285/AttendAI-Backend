from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
)
from app.services.employee_service import (
    create_employee_service,
    get_all_employees_service,
    get_employee_service,
    update_employee_service,
    delete_employee_service,
)
from app.security import require_roles

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(["Admin", "HR"])),
):
    return create_employee_service(db, employee)


@router.get(
    "/",
    response_model=List[EmployeeResponse],
)
def get_all_employees(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(["Admin", "HR", "Manager"])),
):
    return get_all_employees_service(db)


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(["Admin", "HR", "Manager"])),
):
    return get_employee_service(db, employee_id)


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(["Admin", "HR"])),
):
    return update_employee_service(db, employee_id, employee)


@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_200_OK,
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(["Admin"])),
):
    delete_employee_service(db, employee_id)

    return {
        "message": "Employee deleted successfully"
    }