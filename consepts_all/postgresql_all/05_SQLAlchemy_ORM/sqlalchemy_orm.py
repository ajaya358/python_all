# SQLAlchemy ORM - Python way to work with databases
# ORM = Object Relational Mapper: Python class = DB table
# pip install sqlalchemy psycopg2-binary

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from sqlalchemy.sql import func

# --- Database connection ---
DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydb"
# For SQLite (no install needed for testing):
# DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# --- Models (Python class = DB table) ---
class User(Base):
    __tablename__ = "users"
    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String(100), nullable=False)
    email    = Column(String(150), unique=True, nullable=False)
    age      = Column(Integer)
    created  = Column(DateTime, default=func.now())
    orders   = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id       = Column(Integer, primary_key=True, index=True)
    user_id  = Column(Integer, ForeignKey("users.id"))
    product  = Column(String(100))
    amount   = Column(Float)
    user     = relationship("User", back_populates="orders")

# Create all tables
Base.metadata.create_all(bind=engine)

# --- CRUD Operations ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
def create_user(db: Session, name: str, email: str, age: int):
    user = User(name=name, email=email, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# READ
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# UPDATE
def update_user(db: Session, user_id: int, name: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        db.commit()
        db.refresh(user)
    return user

# DELETE
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

# --- Usage Example ---
print("SQLAlchemy ORM ready.")
print("Tables: users, orders")
print("Operations: create_user, get_user, get_all_users, update_user, delete_user")
print("\nConnect to FastAPI using Depends(get_db) in route functions")
