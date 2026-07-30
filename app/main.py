from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.security import get_current_user, require_roles
from app.crud.user import (
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
)
from app.schemas.user import UserUpdate, UserResponse
from app.services.user_service import profile_service

from app.controllers import auth

print("Models Loaded:", Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AttendAI Backend",
    description="Backend API for AttendAI Internship Project",
    version="1.0.0",
)

app.include_router(auth.router)


@app.get(
    "/",
    tags=["Home"],
    summary="Welcome",
    description="Welcome endpoint of AttendAI Backend."
)
def root():
    return {"message": "Welcome to AttendAI Backend"}


@app.get(
    "/db-test",
    tags=["Database"],
    summary="Database Connection Test",
    description="Checks whether the PostgreSQL database is connected successfully."
)
def db_test():
    try:
        connection = engine.connect()
        connection.close()
        return {"message": "Database Connected Successfully ✅"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get(
    "/profile",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Get My Profile",
    description="Returns the profile details of the currently logged-in user."
)
def profile(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return profile_service(db, current_user)


@app.get(
    "/users",
    response_model=List[UserResponse],
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Get All Users",
    description="Returns all registered users. Accessible by Admin, HR and Manager."
)
def users(
    current_user=Depends(require_roles(["Admin", "HR", "Manager"])),
    db: Session = Depends(get_db),
):
    return get_users(db)


@app.get(
    "/users/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Get User by ID",
    description="Returns details of a specific user."
)
def user_by_id(
    user_id: int,
    current_user=Depends(require_roles(["Admin", "HR", "Manager"])),
    db: Session = Depends(get_db),
):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@app.put(
    "/users/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Update User",
    description="Updates an existing user's details. Accessible by Admin and HR."
)
def update_user_api(
    user_id: int,
    user: UserUpdate,
    current_user=Depends(require_roles(["Admin", "HR"])),
    db: Session = Depends(get_db),
):
    updated_user = update_user(db, user_id, user)

    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user


@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Delete User",
    description="Deletes a user from the system. Accessible only by Admin."
)
def delete(
    user_id: int,
    current_user=Depends(require_roles(["Admin"])),
    db: Session = Depends(get_db),
):
    deleted = delete_user(db, user_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }