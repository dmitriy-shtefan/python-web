from fastapi import FastAPI

from .routers import courses
from .routers import auth


app = FastAPI()

app.include_router(auth.router, tags=['auth'])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
