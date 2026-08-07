from sqlalchemy import Column, Integer, String, Date, Time, DateTime
from datetime import datetime

from app.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    check_in = Column(Time)
    check_out = Column(Time)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)