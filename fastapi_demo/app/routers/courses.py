from fastapi import Depends
from fastapi import APIRouter
from fastapi import status

from ..dependencies import get_course_or_not_found
from ..schemas import CourseCreate
from ..schemas import Course
from ..data import courses

router = APIRouter()


@router.get('/list', response_model=list[Course])
async def courses_list():
    return courses


@router.get('/search', response_model=list[Course])
async def courses_search(level: str | None = None):
    if level is None:
        return courses

    result = []
    for course in courses:
        if course['level'] == level:
            result.append(course)

    return result


@router.get('/{course_id}', response_model=Course)
async def course_get(course= Depends(get_course_or_not_found)):
    return course




@router.post('/', response_model=CourseCreate, status_code=status.HTTP_201_CREATED)
async def course_create(course: Course):
    new_course = {
        'id': len(courses) + 1,
        'title': course.title,
        'level': course.level,
        'hours': course.hours,
    }
    courses.append(new_course)
    return new_course