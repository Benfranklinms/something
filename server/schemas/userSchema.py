from pydantic import BaseModel, EmailStr

class UserSignup(BaseModel):
    email: EmailStr  # Ensures valid email format
    password: str
    role: str = "user"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "securepassword123",
                "role": "user"
            }
        }

class UserLogin(BaseModel):
    email: EmailStr
    password: str