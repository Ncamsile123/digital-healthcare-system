from fastapi import APIRouter, UploadFile, File
import shutil
import os
import cv2

router = APIRouter(
    prefix="/faces",
    tags=["Facial Recognition"]
)
@router.post("/register")
async def register_face(
    patient_id: int,
    image: UploadFile = File(...)
):
    os.makedirs("media/faces", exist_ok=True)

    file_path = f"media/faces/patient_{patient_id}.jpg"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        "message": "Face registered successfully",
        "file": file_path
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

    stored = cv2.imread(registered_image)
    checkin = cv2.imread(temp_file)

    if stored is None or checkin is None:
        return {
            "verified": False,
            "message": "Image could not be processed"
        }

    print("Stored shape:", stored.shape)
    print("Checkin shape:", checkin.shape)

    stored = cv2.cvtColor(stored, cv2.COLOR_BGR2GRAY)
    checkin = cv2.cvtColor(checkin, cv2.COLOR_BGR2GRAY)

    stored = cv2.resize(stored, (300, 300))
    checkin = cv2.resize(checkin, (300, 300))

    difference = cv2.absdiff(stored, checkin)

    score = float(difference.mean())

    confidence = max(0.0, 100.0 - score)

    verified = bool(confidence > 70)

    return {
        "patient_id": int(patient_id),
        "verified": verified,
        "confidence": round(confidence, 2)
    }