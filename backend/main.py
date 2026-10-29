from fastapi import FastAPI
import models
from database import engine
from routers import patients, appointments, billing, medical_records, auth, reports, sicknotes, facial_recognition
import reminder_scheduler
from fastapi.middleware.cors import CORSMiddleware


# Create FastAPI app instance
app = FastAPI(title="Digital Healthcare System")

app.add_middleware(
CORSMiddleware,
allow_origins=[
"http://localhost:3000",
"http://127.0.0.1:3000",
],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(billing.router)
app.include_router(medical_records.router)
app.include_router(auth.router)
app.include_router(reports.router, prefix="/reports", tags=["Reports"])
app.include_router(sicknotes.router)
app.include_router(facial_recognition.router)
# Start reminder scheduler when app starts
#@app.on_event("startup")
#def startup_event():
 #   reminder_scheduler.scheduler.start()

#@app.on_event("shutdown")
#def shutdown_event():
 #   reminder_scheduler.scheduler.shutdown()

@app.get("/")
def home():
    return {"message": "Healthcare System API Running"}
