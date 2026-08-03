from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(String(20), unique=True, nullable=False)

    first_name = Column(String(50), nullable=False)

    last_name = Column(String(50), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    phone = Column(String(15), nullable=False)

    department = Column(String(50), nullable=False)

    designation = Column(String(50), nullable=False)

    joining_date = Column(Date, nullable=False)

    salary = Column(Float, nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())