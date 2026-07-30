from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.security import hash_password


def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        employee_id=user.employee_id,
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role,
        department=user.department,
        phone=user.phone,
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_profile(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def update_user(db: Session, user_id: int, user: UserUpdate):
    existing_user = db.query(User).filter(User.id == user_id).first()

    if existing_user is None:
        return None

    existing_user.username = user.username
    existing_user.email = user.email
    existing_user.department = user.department
    existing_user.phone = user.phone
    existing_user.role = user.role

    db.commit()
    db.refresh(existing_user)

    return existing_user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None

    db.delete(user)
    db.commit()

    return user