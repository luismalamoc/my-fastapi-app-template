from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserRead
from app.context import app_context
from app.config.database import get_db

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = app_context.get_user_service(db)
    db_user = user_service.create_user(db, user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User could not be created")
    return db_user
