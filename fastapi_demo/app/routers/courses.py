import logging

from fastapi import APIRouter
from fastapi import HTTPException

from ..data import courses
from ..schemas import Course
from ..schemas import CourseCreate


router = APIRouter()
logger = logging.getLogger("app.courses")


@router.get("/courses/list", response_model=list[Course])
def courses_list():
    logger.debug("courses list requested count=%s", len(courses))
    return courses


@router.get("/courses/search", response_model=Course)
def courses_search(level: str):
    logger.info("course search started level=%s", level)

    for course in courses:
        if course["level"] == level:
            logger.info("course search matched level=%s course_id=%s", level, course["id"])
            return course

    logger.warning("course search missed level=%s", level)
    raise HTTPException(status_code=404, detail="Course not found")


@router.get("/courses/{course_id}", response_model=Course)
def courses_detail(course_id: int):
    logger.info("course detail requested course_id=%s", course_id)

    for course in courses:
        if course["id"] == course_id:
            logger.debug("course detail found course_id=%s", course_id)
            return course

    logger.warning("course detail not found course_id=%s", course_id)
    raise HTTPException(status_code=404, detail="Course not found")



@router.post("/courses", response_model=Course)
def courses_create(course: CourseCreate):
    logger.info("course create requested title=%s level=%s", course.title, course.level)

    new_course = {
        "id": len(courses) + 1,
        "title": course.title,
        "level": course.level,
        "hours": course.hours
    }
    courses.append(new_course)

    logger.info("course created course_id=%s total_courses=%s", new_course["id"], len(courses))

    return new_course


# versions
# 0.1.0    0: major   1: minor   0: patch
# 1.0.0    1: major   0: minor   0: patch
# 2.0.0    2: major   0: minor   0: patch
