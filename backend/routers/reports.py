from fastapi import APIRouter, Depends
from routers.billing import get_db
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import func
from database import Base, engine
import models
import schemas


router = APIRouter()

@router.get("/summary", response_model=schemas.ReportSummary)
def get_summary(db: Session = Depends(get_db)):

    total_patients = db.query(models.Patient).count()

    one_week_ago = datetime.now() - timedelta(days=7)

    appointments_last_week = (
        db.query(models.Appointment)
        .filter(models.Appointment.appointment_date >= one_week_ago)
        .count()
    )

    total_billing = db.query(
        func.sum(models.Billing.amount)
    ).scalar() or 0

    print("Patients:", total_patients)
    print("Appointments:", appointments_last_week)
    print("Billing:", total_billing)

    return schemas.ReportSummary(
        total_patients=total_patients,
        appointments_last_week=appointments_last_week,
        total_billing=float(total_billing)
    )