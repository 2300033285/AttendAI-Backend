from sqlalchemy.orm import Session

from app.crud.insights import get_insights


def insights_service(db: Session):
    return get_insights(db)