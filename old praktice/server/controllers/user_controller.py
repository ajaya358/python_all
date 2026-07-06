from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, LoginRequest
from auth.jwt import create_access_token
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(payload: UserCreate, db: Session):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = pwd_context.hash(payload.password)
    new_user = User(
        name=payload.name,
        email=payload.email,
        password=hashed_pwd,
        role=payload.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(payload: LoginRequest, db: Session):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not pwd_context.verify(payload.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id), "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
