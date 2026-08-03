from pydantic import BaseModel, EmailStr
from datetime import date


class EmployeeCreate(BaseModel):
    employee_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    department: str
    designation: str
    joining_date: date
    salary: float


class EmployeeUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    department: str
    designation: str
    joining_date: date
    salary: float
    status: bool


class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    department: str
    designation: str
    joining_date: date
    salary: float
    status: bool

    class Config:
        from_attributes = True