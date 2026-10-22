from pydantic import BaseModel

class ReportSummary(BaseModel):
    total_patients: int
    appointments_last_week: int
    total_billing: float
