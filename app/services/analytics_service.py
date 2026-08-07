from sqlalchemy.orm import Session

from app.crud.analytics import get_analytics


def analytics_service(db: Session):
    return get_analytics(db)
