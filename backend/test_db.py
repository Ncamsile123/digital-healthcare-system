from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:your_password@localhost/healthcare_db"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("✅ Connected to PostgreSQL successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
