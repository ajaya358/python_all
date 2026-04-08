from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import psycopg2
import os

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Parse DB name and connection params
import urllib.parse as up
up.uses_netloc.append("postgres")
url = up.urlparse(DATABASE_URL)

db_name = url.path[1:]  # remove the leading "/"
admin_db_url = f"postgresql://{url.username}:{url.password}@{url.hostname}:{url.port}/postgres"

# Step 1: Connect to default DB and create target DB if missing
try:
    conn = psycopg2.connect(admin_db_url)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(f'CREATE DATABASE "{db_name}"')
        print(f"Database '{db_name}' created.")
    else:
        print(f"Database '{db_name}' already exists.")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error while checking/creating DB: {e}")

# Step 2: SQLAlchemy setup with your real DB
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to use in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
