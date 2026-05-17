from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    level: str
    hours: int


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
