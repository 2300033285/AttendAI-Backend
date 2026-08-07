from sqlalchemy.orm import Session

from app.crud.ai_prediction import get_ai_prediction


def ai_prediction_service(db: Session):
    return get_ai_prediction(db)