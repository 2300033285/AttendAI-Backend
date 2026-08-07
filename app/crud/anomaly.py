from sqlalchemy.orm import Session

from app.models.attendance import Attendance


def get_anomalies(db: Session):

    late_records = (
        db.query(Attendance)
        .filter(Attendance.status == "Late")
        .all()
    )

    absent_records = (
        db.query(Attendance)
        .filter(Attendance.status == "Absent")
        .all()
    )

    anomalies = []

    for record in late_records:
        anomalies.append({
            "attendance_id": record.id,
            "user_id": record.user_id,
            "status": record.status
        })

    for record in absent_records:
        anomalies.append({
            "attendance_id": record.id,
            "user_id": record.user_id,
            "status": record.status
        })

    return {
        "total_anomalies": len(anomalies),
        "anomalies": anomalies
    }