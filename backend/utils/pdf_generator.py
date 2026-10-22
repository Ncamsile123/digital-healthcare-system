from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os


def generate_sicknote_pdf(
    output_path,
    patient_name,
    id_number,
    diagnosis,
    consultation_date,
    sick_from,
    sick_to,
    doctor_name,
    practice_number
):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "MEDICAL SICK NOTE")

    c.setStrokeColor(colors.black)
    c.line(50, height - 60, 550, height - 60)

    # Patient Details
    c.setFont("Helvetica", 12)
    y = height - 100

    c.drawString(50, y, f"Patient Name: {patient_name}")
    y -= 25

    c.drawString(50, y, f"ID Number: {id_number}")
    y -= 25

    c.drawString(50, y, f"Consultation Date: {consultation_date}")
    y -= 40

    c.drawString(
        50,
        y,
        f"This serves to certify that the above patient was examined and is medically unfit for work."
    )
    y -= 30

    c.drawString(50, y, f"Diagnosis: {diagnosis}")
    y -= 25

    c.drawString(50, y, f"Sick Leave Period: {sick_from} to {sick_to}")
    y -= 60

    # Signature
    signature_path = "media/signatures/signature.webp"

    if os.path.exists(signature_path):
        c.drawImage(
            signature_path,
            50,
            y - 20,
            width=120,
            height=50,
            mask='auto'
        )

    c.drawString(50, y - 40, f"Doctor: {doctor_name}")
    c.drawString(50, y - 60, f"Practice No: {practice_number}")

    # Stamp
    stamp_path = "media/stamps/clinic stamp.png"

    if os.path.exists(stamp_path):
        c.drawImage(
            stamp_path,
            350,
            y - 60,
            width=120,
            height=120,
            mask='auto'
        )

    c.save()

    return output_path