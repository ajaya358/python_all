from fastapi import APIRouter, Depends, Request, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.db import get_login_db
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service
from app.core.security import get_current_user
from app.core.limiter import limiter
from app.tasks.background_tasks import send_welcome_email

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
@limiter.limit("3/minute")
def create_user(request: Request, user: UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_login_db)):
    new_user = user_service.create_user(db, user)
    background_tasks.add_task(send_welcome_email, new_user.email, new_user.name)
    return new_user

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_login_db), current_user: dict = Depends(get_current_user)):
    return user_service.get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_login_db), current_user: dict = Depends(get_current_user)):
    return user_service.get_user(db, user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_login_db), current_user: dict = Depends(get_current_user)):
    return user_service.update_user(db, user_id, user)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_login_db), current_user: dict = Depends(get_current_user)):
    return user_service.delete_user(db, user_id)
