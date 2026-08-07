from sqlalchemy.orm import Session

from app.crud.dashboard import get_dashboard_stats


def dashboard_service(db: Session):
    return get_dashboard_stats(db)