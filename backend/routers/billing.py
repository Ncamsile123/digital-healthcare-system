from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models

from datetime import datetime

router = APIRouter(prefix="/billing", tags=["Billing"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create Billing Record
@router.post("/")
def create_billing(
    patient_id: int,
    amount: float,
    status: str = "Pending",
    db: Session = Depends(get_db)
):
    # Check patient exists
    patient = db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    new_billing = models.Billing(
        patient_id=patient_id,
        amount=amount,
        invoice_date=datetime.utcnow().date(),  # ✅ matches DB column
        status=status
    )
    db.add(new_billing)
    db.commit()
    db.refresh(new_billing)
    return {
        "message": "Billing record created successfully",
        "billing_id": new_billing.billing_id,
        "amount": float(new_billing.amount),
        "status": new_billing.status,
        "invoice_date": str(new_billing.invoice_date)
    }

# ✅ Retrieve Billing by ID
@router.get("/{billing_id}")
def get_billing(billing_id: int, db: Session = Depends(get_db)):
    billing = db.query(models.Billing).filter(models.Billing.billing_id == billing_id).first()
    if not billing:
        raise HTTPException(status_code=404, detail="Billing record not found")
    return {
        "billing_id": billing.billing_id,
        "patient_id": billing.patient_id,
        "amount": float(billing.amount),
        "status": billing.status,
        "invoice_date": str(billing.invoice_date)
    }

# ✅ List All Billing Records for a Patient
@router.get("/patient/{patient_id}")
def list_billing_for_patient(patient_id: int, db: Session = Depends(get_db)):
    billings = db.query(models.Billing).filter(models.Billing.patient_id == patient_id).all()
    if not billings:
        raise HTTPException(status_code=404, detail="No billing records found for this patient")
    return [
        {
            "billing_id": bill.billing_id,
            "amount": float(bill.amount),
            "status": bill.status,
            "invoice_date": str(bill.invoice_date)
        }
        for bill in billings
    ]
