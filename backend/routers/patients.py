from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter(prefix="/patients", tags=["Patients"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create Patient
@router.post("/")
def create_patient(first_name: str, last_name: str, phone_number: str, db: Session = Depends(get_db)):
    new_patient = models.Patient(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return {"message": "Patient created successfully", "patient_id": new_patient.patient_id}

# ✅ Retrieve Patient by ID
@router.get("/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {
        "patient_id": patient.patient_id,
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "phone_number": patient.phone_number,
        "date_of_birth": str(patient.date_of_birth) if patient.date_of_birth else None,
        "gender": patient.gender,
        "national_id": patient.national_id,
        "created_at": str(patient.created_at) if patient.created_at else None
    }
