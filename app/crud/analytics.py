from sqlalchemy.orm import Session
from app.models.attendance import Attendance


def get_analytics(db: Session):
    records = db.query(Attendance).all()
    

    if not records:
        return {
            "attendance_percentage": 0,
            "present_days": 0,
            "absent_days": 0,
            "late_count": 0,
            "average_hours": 0
        }

    total_records = len(records)

    present_days = sum(
        1 for record in records
        if record.status.lower() == "present"
    )

    absent_days = sum(
        1 for record in records
        if record.status.lower() == "absent"
    )

    attendance_percentage = (
        (present_days / total_records) * 100
        if total_records > 0 else 0
    )

    # Calculate average working hours
    total_hours = 0
    working_records = 0

    for record in records:
        if (
            record.status.lower() == "present"
            and record.check_in
            and record.check_out
        ):
            check_in = (
                record.check_in.hour +
                record.check_in.minute / 60
            )

            check_out = (
                record.check_out.hour +
                record.check_out.minute / 60
            )

            total_hours += (check_out - check_in)
            working_records += 1

    average_hours = (
        round(total_hours / working_records, 2)
        if working_records > 0 else 0
    )

    # Calculate late count (after 9:00 AM)
    late_count = 0

    for record in records:
        if (
            record.status.lower() == "present"
            and record.check_in
        ):
            if (
                record.check_in.hour > 9 or
                (
                    record.check_in.hour == 9
                    and record.check_in.minute > 0
                )
            ):
                late_count += 1

    return {
        "attendance_percentage": round(attendance_percentage, 2),
        "present_days": present_days,
        "absent_days": absent_days,
        "late_count": late_count,
        "average_hours": average_hours,
    }