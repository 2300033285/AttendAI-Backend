from pydantic import BaseModel
from typing import Dict


class InsightsResponse(BaseModel):
    total_employees: int
    active_employees: int
    attendance_percentage: float
    department_summary: Dict[str, int]
    designation_summary: Dict[str, int]