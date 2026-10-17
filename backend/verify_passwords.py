from passlib.context import CryptContext
from database import SessionLocal
import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = SessionLocal()

users = db.query(models.User).all()
for user in users:
    print(f"Checking {user.username}...")
    for plain in ["adminpassword", "doctorpassword", "nursepassword"]:
        if pwd_context.verify(plain, user.password_hash):
            print(f"  Matches: {plain}")
