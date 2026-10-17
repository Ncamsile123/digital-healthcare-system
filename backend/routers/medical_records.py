# routers/medical_records.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from datetime import datetime

router = APIRouter(prefix="/medical_records", tags=["Medical Records"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create Medical Record
@router.post("/")
def create_medical_record(
    patient_id: int,
    diagnosis: str,
    treatment: str,
    notes: str = None,
    db: Session = Depends(get_db)
):
    # Check patient exists
    patient = db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    new_record = models.MedicalRecord(
        patient_id=patient_id,
        diagnosis=diagnosis,
        treatment=treatment,
        notes=notes,
        created_at=datetime.utcnow()
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {
        "message": "Medical record created successfully",
        "record_id": new_record.record_id,
        "patient_id": new_record.patient_id,
        "diagnosis": new_record.diagnosis,
        "treatment": new_record.treatment
    }

# ✅ Get All Records for a Patient
@router.get("/patient/{patient_id}")
def list_medical_records(patient_id: int, db: Session = Depends(get_db)):
    records = db.query(models.MedicalRecord).filter(models.MedicalRecord.patient_id == patient_id).all()
    if not records:
        raise HTTPException(status_code=404, detail="No medical records found for this patient")
    return [
        {
            "record_id": rec.record_id,
            "diagnosis": rec.diagnosis,
            "treatment": rec.treatment,
            "notes": rec.notes,
            "created_at": str(rec.created_at)
        }
        for rec in records
    ]
