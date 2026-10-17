from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from datetime import datetime

router = APIRouter(prefix="/appointments", tags=["Appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create Appointment
@router.post("/")
def create_appointment(patient_id: int, appointment_date: datetime, db: Session = Depends(get_db)):
    # Check patient exists
    patient = db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    new_appointment = models.Appointment(
        patient_id=patient_id,
        appointment_date=appointment_date,
        status="Scheduled"
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return {"message": "Appointment created successfully", "appointment_id": new_appointment.appointment_id}

# ✅ Retrieve Appointment by ID
@router.get("/{appointment_id}")
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {
        "appointment_id": appointment.appointment_id,
        "patient_id": appointment.patient_id,
        "appointment_date": str(appointment.appointment_date),
        "status": appointment.status
    }

# ✅ List All Appointments for a Patient
@router.get("/patient/{patient_id}")
def list_appointments_for_patient(patient_id: int, db: Session = Depends(get_db)):
    appointments = db.query(models.Appointment).filter(models.Appointment.patient_id == patient_id).all()
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found for this patient")
    return [
        {
            "appointment_id": appt.appointment_id,
            "appointment_date": str(appt.appointment_date),
            "status": appt.status
        }
        for appt in appointments
    ]
