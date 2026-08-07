from pydantic import BaseModel
from datetime import date, time, datetime
from typing import Optional


class AttendanceCreate(BaseModel):
    user_id: int
    date: date
    check_in: time
    check_out: time
    status: str


class AttendanceUpdate(BaseModel):
    check_in: Optional[time] = None
    check_out: Optional[time] = None
    status: Optional[str] = None


class AttendanceResponse(BaseModel):
    id: int
    user_id: int
    date: date
    check_in: Optional[time]
    check_out: Optional[time]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True