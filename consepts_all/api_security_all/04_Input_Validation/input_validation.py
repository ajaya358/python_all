# Input Validation & SQL Injection Prevention
# Never trust user input — always validate and sanitize

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
import re

app = FastAPI()

# --- Pydantic validation (prevents bad input) ---
class UserInput(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: str = Field(max_length=150)
    age: int = Field(ge=0, le=120)
    phone: str = Field(max_length=15)

    @validator("email")
    def validate_email(cls, v):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not re.match(pattern, v):
            raise ValueError("Invalid email format")
        return v.lower()

    @validator("phone")
    def validate_phone(cls, v):
        if not re.match(r'^\+?[\d\s\-]{7,15}$', v):
            raise ValueError("Invalid phone number")
        return v

    @validator("name")
    def validate_name(cls, v):
        if not re.match(r'^[a-zA-Z\s]+$', v):
            raise ValueError("Name must contain only letters")
        return v.strip()

@app.post("/users")
def create_user(user: UserInput):
    return {"message": f"User {user.name} created", "email": user.email}

# --- SQL Injection Prevention ---
print("=== SQL Injection ===")
print("""
# DANGEROUS - Never do this (SQL injection possible)
name = "Ajay' OR '1'='1"
query = f"SELECT * FROM users WHERE name = '{name}'"
# This becomes: SELECT * FROM users WHERE name = 'Ajay' OR '1'='1'
# Returns ALL users!

# SAFE - Use parameterized queries (SQLAlchemy does this automatically)
from sqlalchemy.orm import Session
def get_user(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()
    # SQLAlchemy escapes the input automatically

# SAFE - Raw SQL with parameters
db.execute("SELECT * FROM users WHERE name = :name", {"name": name})
""")

print("=== Other Validation Tips ===")
tips = [
    "Validate file uploads: check extension AND mime type",
    "Limit file upload size",
    "Strip HTML tags from text inputs to prevent XSS",
    "Never eval() user input",
    "Validate URL parameters — don't trust path params",
    "Use UUID instead of sequential IDs to prevent IDOR",
]
for t in tips:
    print(f"  - {t}")

# Run: uvicorn input_validation:app --reload
