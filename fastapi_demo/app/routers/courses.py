from fastapi import APIRouter
from fastapi import HTTPException

from ..data import courses
from ..schemas import Course
from ..schemas import CourseCreate


router = APIRouter()

@router.get("/courses/list", response_model=list[Course])
def courses_list():
    return courses


@router.get("/courses/search", response_model=Course)
def courses_search(level: str):
    for course in courses:
        if course["level"] == level:
            return course

    return HTTPException(status_code=404, detail="Course not found")


@router.get("/courses/{course_id}", response_model=Course)
def courses_detail(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course

    return HTTPException(status_code=404, detail="Course not found")



@router.post("/courses", response_model=Course)
def courses_create(course: CourseCreate):
    new_course = {
        "id": len(courses) + 1,
        "title": course.title,
        "level": course.level,
        "hours": course.hours
    }
    courses.append(new_course)

    return new_course


# versions
# 0.1.0    0: major   1: minor   0: patch
# 1.0.0    1: major   0: minor   0: patch
# 2.0.0    2: major   0: minor   0: patch