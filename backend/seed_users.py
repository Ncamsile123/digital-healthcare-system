from database import SessionLocal
import models
from datetime import datetime
from routers.auth import safe_hash   # adjust import if auth.py is in routers/

db = SessionLocal()

def add_user(username, password, role):
    hashed_pw = safe_hash(password)   # ✅ ensures bcrypt hash
    user = models.User(
        username=username,
        password_hash=hashed_pw,
        role=role,
        created_at=datetime.utcnow()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"✅ Added {role}: {username} (id={user.user_id})")

add_user("admin1", "adminpassword", "admin")
add_user("doctor1", "doctorpassword", "doctor")
add_user("nurse1", "nursepassword", "nurse")

db.close()
