from fastapi import APIRouter, Depends

from app.data import courses
from app.dependencies import get_course_or_404, get_current_teacher
from app.schemas import CourseCreate, User

router = APIRouter()


@router.get("/items")
def get_items():
    return courses


@router.get("/items/{item_id}")
def get_item(course: dict = Depends(get_course_or_404)):
    return course


@router.get("/search")
def search_items(level: str | None = None):
    if level is None:
        return courses

    result = []
    for course in courses:
        if course["level"] == level:
            result.append(course)

    return result


@router.post("/items")
def create_item(
    course: CourseCreate,
    current_user: User = Depends(get_current_teacher),
):
    new_course = {
        "id": len(courses) + 1,
        "title": course.title,
        "level": course.level,
        "hours": course.hours,
        "created_by": current_user.username,
    }
    courses.append(new_course)
    return new_course
