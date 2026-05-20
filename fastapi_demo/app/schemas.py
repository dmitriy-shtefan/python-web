from pydantic import BaseModel
from pydantic import Field

class Course(BaseModel):
    name: str
    description: str = Field(default='description', description='description in the docs and redoc')