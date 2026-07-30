from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    employee_id: str
    username: str
    email: EmailStr
    password: str
    department: str
    phone: str
    role: str = "Employee"


class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    department: str
    phone: str
    role: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    employee_id: str
    username: str
    email: EmailStr
    department: str
    phone: str
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str