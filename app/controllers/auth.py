from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserLogin, Token
from app.services.auth_service import register_service, login_service

router = APIRouter(tags=["Authentication"])


@router.post(
    "/register",
    tags=["Authentication"],
    summary="Register a New User",
    description="Creates a new user account in the AttendAI system."
)
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = register_service(db, user)

    return {
        "message": "User Registered Successfully",
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role,
    }


@router.post(
    "/login",
    response_model=Token,
    tags=["Authentication"],
    summary="User Login",
    description="Authenticates a user and returns a JWT access token."
)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_service(db, user)