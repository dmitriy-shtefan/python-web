from pydantic import BaseModel
from pydantic import field_validator
from pydantic import Field


class CourseCreate(BaseModel):
    title: str = Field(..., description='course title')  # required
    level: str = Field(default='beginner', description='entry level description')
    hours: int = Field(default=0)

    @field_validator('level')
    @classmethod
    def level_validator(cls, v):
        allowed_values = ['beginner', 'intermediate', 'expert']

        if v not in allowed_values:
            raise ValueError('Invalid course level')
        return v


class Course(CourseCreate):
    id: int = Field(description='course id')


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str


class User(BaseModel):
    username: str