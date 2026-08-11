

from fastapi import APIRouter
router = APIRouter(
    prefix="/students",
    tags=["Students"]
)
from models.schemas.student_schema import StudentCreate
from models.services.student_services import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)


@router.get("/")
def get_students():
    return get_all_students()


@router.get("/{student_id}")
def get_student(student_id: str):
    return get_student_by_id(student_id)


@router.post("/")
def add_student(student: StudentCreate):
    return create_student(student)
@router.put("/{student_id}")
def edit_student(student_id: str, updated_data: dict):
    return update_student(student_id, updated_data)


@router.delete("/{student_id}")
def remove_student(student_id: str):
    return delete_student(student_id)