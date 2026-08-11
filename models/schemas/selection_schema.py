from pydantic import BaseModel, Field


class SelectionCreate(BaseModel):
    number_student: str = Field(min_length=3, max_length=20)
    course_id: int