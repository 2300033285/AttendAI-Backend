from pydantic import BaseModel


class EmployeeAnalyticsResponse(BaseModel):
    total_employees: int
    active_employees: int
    inactive_employees: int
    department_count: dict
    designation_count: dict