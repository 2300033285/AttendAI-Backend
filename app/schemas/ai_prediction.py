from pydantic import BaseModel


class AIPredictionResponse(BaseModel):
    prediction: str
    confidence: float