from fastapi import APIRouter
router = APIRouter(
    prefix="/professors",
    tags=["Professors"]
)
from models.schemas.professor_schema import ProfessorCreate

from models.services.professor_services import (
    create_professor,
    get_all_professors,
    get_professor_by_id,
    update_professor,
    delete_professor
)


@router.get("/")
def get_professors():
    return get_all_professors()

@router.get("/{code_personnel}")
def get_professor(code_personnel: str):
    return get_professor_by_id(code_personnel)

@router.post("/")
def add_professor(professor: ProfessorCreate):
    return create_professor(professor)

@router.put("/{code_personnel}")
def edit_professor(code_personnel: str, updated_data: dict):
    return update_professor(code_personnel, updated_data)

@router.delete("/{code_personnel}")
def remove_professor(code_personnel: str):
    return delete_professor(code_personnel)