from fastapi import HTTPException
from fastapi import status

from .data import courses


def get_course_or_not_found(course_id: int):
    for course in courses:
        if course['id'] == course_id:
            return course

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)