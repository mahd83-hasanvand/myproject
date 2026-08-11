from fastapi import APIRouter
router = APIRouter(
    prefix="/selections",
    tags=["Selections"]
)
from models.schemas.selection_schema import SelectionCreate
from models.services.selection_services import (
    create_selection,
    get_all_selections,
    delete_selection,
    get_student_courses
)


@router.get("/")
def get_selections():
    return get_all_selections()


@router.post("/")
def add_selection(selection: SelectionCreate):
    return create_selection(selection)


@router.delete("/{student_id}/{course_id}")
def remove_selection(student_id: str, course_id: int):
    return delete_selection(student_id, course_id)

@router.get("/students/{student_id}/courses")
def student_courses(student_id: str):
    return get_student_courses(student_id)