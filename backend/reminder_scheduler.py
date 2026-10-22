from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from database import SessionLocal   # ✅ import SessionLocal correctly
import models
from datetime import datetime
import sms_gateway   # ✅ cleaner import

def send_pending_reminders():
    db: Session = SessionLocal()
    now = datetime.utcnow()

    reminders = db.query(models.SMSReminder).filter(
        models.SMSReminder.scheduled_time <= now,
        models.SMSReminder.sent == False
    ).all()

    for reminder in reminders:
        sms_gateway.send_sms(reminder.phone_number, reminder.message)
        reminder.sent = True
        db.commit()

    db.close()

# ✅ create scheduler instance but don’t start it here
scheduler = BackgroundScheduler()
scheduler.add_job(send_pending_reminders, "interval", minutes=5)
