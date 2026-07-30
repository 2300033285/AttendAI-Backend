from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.user import (
    get_profile,
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
)
from app.schemas.user import UserUpdate


def profile_service(db: Session, current_user):
    user = get_profile(db, current_user["sub"])

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def get_all_users_service(db: Session):
    return get_users(db)


def get_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def update_user_service(db: Session, user_id: int, user: UserUpdate):
    updated_user = update_user(db, user_id, user)

    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user


def delete_user_service(db: Session, user_id: int):
    deleted_user = delete_user(db, user_id)

    if deleted_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return deleted_user