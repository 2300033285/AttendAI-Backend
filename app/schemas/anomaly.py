from pydantic import BaseModel
from typing import List


class Anomaly(BaseModel):
    attendance_id: int
    user_id: int
    status: str


class AnomalyResponse(BaseModel):
    total_anomalies: int
    anomalies: List[Anomaly]