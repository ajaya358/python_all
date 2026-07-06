from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.hashing import hash_password
from app.core.exceptions import BadRequestException, NotFoundException

def create_user(db: Session, user: UserCreate):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise BadRequestException("Email already registered")
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundException(f"User with id {user_id} not found")
    return user

def update_user(db: Session, user_id: int, user: UserCreate):
    db_user          = get_user(db, user_id)
    db_user.name     = user.name
    db_user.email    = user.email
    db_user.password = hash_password(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}
