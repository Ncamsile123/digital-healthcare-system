from passlib.context import CryptContext
from backend.database import Base, engine
from backend import models


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = SessionLocal()

# Define your plain passwords
users_plain = {
    "admin1": "adminpassword",
    "doctor1": "doctorpassword",
    "nurse1": "nursepassword"
}

for username, plain in users_plain.items():
    user = db.query(models.User).filter(models.User.username == username).first()
    if user:
        user.password_hash = pwd_context.hash(plain)
        print(f"Updated {username} with new hash")
    else:
        print(f"User {username} not found")

db.commit()
db.close()
