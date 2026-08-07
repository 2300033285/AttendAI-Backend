from sqlalchemy.orm import Session

from app.crud.anomaly import get_anomalies


def anomaly_service(db: Session):
    return get_anomalies(db)