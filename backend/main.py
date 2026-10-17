from fastapi import FastAPI
from database import Base, engine
import models
from routers import patients, appointments, billing, medical_records, auth   # ✅ add medical_records

# Create FastAPI app instance
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(billing.router)
app.include_router(medical_records.router)  # ✅ register medical_records
app.include_router(auth.router)  # ✅ register auth
@app.get("/")
def home():
    return {"message": "Healthcare System API Running"}


