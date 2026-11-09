from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import get_db
from deepface import DeepFace

import models
import shutil
import os
import cv2

router = APIRouter(
    prefix="/faces",
    tags=["Facial Recognition"]
)
@router.post("/register/{patient_id}")
async def register_face(
    patient_id: int,
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    patient = (
        db.query(models.Patient)
        .filter(
            models.Patient.patient_id == patient_id
        )
        .first()
    )

    if not patient:
        return {
            "success": False,
            "message": "Patient not found"
        }

    os.makedirs(
        "media/faces",
        exist_ok=True
    )

    file_path = (
        f"media/faces/patient_{patient_id}.jpg"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        shutil.copyfileobj(
            image.file,
            buffer
        )

    patient.face_image = file_path

    db.commit()

    return {
        "success": True,
        "message": "Face registered successfully"
    }

@router.post("/verify")
async def verify_face(
    patient_id: int,
    image: UploadFile = File(...)
):
    registered_image = f"media/faces/patient_{patient_id}.jpg"

    if not os.path.exists(registered_image):
        return {
            "verified": False,
            "message": "No registered face found"
        }

    temp_file = "media/faces/temp_checkin.jpg"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    try:
        result = DeepFace.verify(
            img1_path=registered_image,
            img2_path=temp_file,
            model_name="Facenet",
            enforce_detection=False
        )

        return {
            "patient_id": patient_id,
            "verified": result["verified"],
            "distance": float(result["distance"])
        }

    except Exception as e:
        return {
            "verified": False,
            "message": str(e)
        }

@router.post("/identify")
async def identify_patient(
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    os.makedirs("media/faces", exist_ok=True)

    temp_file = "media/faces/temp_scan.jpg"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    patients = db.query(models.Patient).all()

    for patient in patients:

        if not patient.face_image:
            continue

        if not os.path.exists(patient.face_image):
            continue

        try:

            result = DeepFace.verify(
                img1_path=patient.face_image,
                img2_path=temp_file,
                model_name="Facenet",
                enforce_detection=False
            )

            if result["verified"]:

                return {
                    "found": True,
                    "confidence": float(1 - result["distance"]),
                    "patient": {
                        "patient_id": patient.patient_id,
                        "first_name": patient.first_name,
                        "last_name": patient.last_name,
                        "phone_number": patient.phone_number,
                        "date_of_birth": patient.date_of_birth,
                        "gender": patient.gender,
                        "national_id": patient.national_id
                    }
                }

        except Exception as e:
            print("DeepFace Error:", e)

    return {
        "found": False,
        "message": "Patient not found"
    }