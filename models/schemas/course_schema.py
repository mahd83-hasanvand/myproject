from pydantic import BaseModel

class CourseCreate(BaseModel):
    course_id: int
    title: str
    code: str
    unit: int
    capacity: int