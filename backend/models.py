from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, DateTime, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime




class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    national_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    password_hash = Column(Text)
    role = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    appointment_date = Column(DateTime, nullable=False)
    status = Column(String(50), default="Scheduled")


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    record_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    diagnosis = Column(String, nullable=False)
    treatment = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Billing(Base):
    __tablename__ = "billing"

    billing_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    amount = Column(DECIMAL(10, 2), nullable=False)
    invoice_date = Column(Date, default=datetime.utcnow)   # ✅ match DB
    status = Column(String(50), default="Pending")


