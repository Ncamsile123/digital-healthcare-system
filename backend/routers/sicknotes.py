from fastapi import APIRouter
from fastapi.responses import FileResponse
from datetime import datetime
import os

from utils.pdf_generator import generate_sicknote_pdf

router = APIRouter(
    prefix="/sicknotes",
    tags=["Sick Notes"]
)


@router.post("/generate")
def generate_sicknote():

    filename = f"sicknote_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    output_path = f"media/sicknotes/{filename}"

    os.makedirs("media/sicknotes", exist_ok=True)

    generate_sicknote_pdf(
        output_path=output_path,
        patient_name="John Doe",
        id_number="9001015009087",
        diagnosis="Viral Infection",
        consultation_date="2026-10-22",
        sick_from="2026-10-22",
        sick_to="2026-10-24",
        doctor_name="Dr N. Kunene",
        practice_number="PR123456"
    )

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename=filename
    )
import os

print("Signature:", os.path.exists("media/signatures/signature.webp"))
print("Stamp:", os.path.exists("media/stamps/clinic stamp.png"))