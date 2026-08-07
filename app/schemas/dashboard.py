from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_employees: int
    active_employees: int
    total_attendance: int
    present: int
    absent: int
    late: int