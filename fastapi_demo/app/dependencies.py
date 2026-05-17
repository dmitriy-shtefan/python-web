from fastapi import Depends, HTTPException

from app.auth import get_current_user
from app.data import courses
from app.schemas import User


def get_course_or_404(item_id: int) -> dict:
    for course in courses:
        if course["id"] == item_id:
            return course

    raise HTTPException(status_code=404, detail="Курс не знайдено")


def get_current_teacher(current_user: User = Depends(get_current_user)) -> User:
    return current_user
