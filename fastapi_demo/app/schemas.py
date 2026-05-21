from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    level: str
    hours: int


class Course(CourseCreate):
    id: int
