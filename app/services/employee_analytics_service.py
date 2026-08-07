from sqlalchemy.orm import Session

from app.crud.employee_analytics import get_employee_analytics


def employee_analytics_service(db: Session):
    return get_employee_analytics(db)