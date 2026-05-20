from fastapi import FastAPI

from .routers import courses
from .routers import auth


app = FastAPI()


app.include_router(auth.router)
app.include_router(courses.router)