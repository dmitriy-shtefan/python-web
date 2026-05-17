from fastapi import FastAPI

from app.routers import auth
from app.routers import courses

app = FastAPI(title="Courses API")

app.include_router(auth.router)
app.include_router(courses.router)


@app.get("/")
def root():
    return {"message": "API працює"}
