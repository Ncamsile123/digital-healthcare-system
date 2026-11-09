from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File,
    Form
)

from sqlalchemy.orm import Session
from database import SessionLocal
import models
import os
import shutil

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
async def create_patient(
    first_name: str = Form(...),
    last_name: str = Form(...),
    phone_number: str = Form(...),
    date_of_birth: str = Form(None),
    gender: str = Form(None),
    national_id: str = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    new_patient = models.Patient(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        date_of_birth=date_of_birth,
        gender=gender,
        national_id=national_id
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    if image:
        os.makedirs("media/faces", exist_ok=True)

        file_path = (
            f"media/faces/patient_{new_patient.patient_id}.jpg"
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        new_patient.face_image = file_path

        db.commit()

    return {
        "message": "Patient created successfully",
        "patient_id": new_patient.patient_id
    }

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
@router.get("/count")
def patient_count(db: Session = Depends(get_db)):
    count = db.query(models.Patient).count()
    return {"count": count}