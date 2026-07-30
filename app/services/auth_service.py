from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.crud.user import create_user, get_user_by_email
from app.schemas.user import UserCreate, UserLogin
from app.security import (
    verify_password,
    create_access_token
)


def register_service(db: Session, user: UserCreate):
    return create_user(db, user)


def login_service(db: Session, user: UserLogin):

    db_user = get_user_by_email(db, user.email)

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Email or Password"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Email or Password"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }