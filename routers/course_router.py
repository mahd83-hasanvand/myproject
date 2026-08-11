from fastapi import APIRouter
router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)
from models.schemas.course_schema import CourseCreate
from models.services.course_services import (
    create_course,
    get_all_courses,
    get_course_by_id,
    update_course,
    delete_course,
    assign_professor,
    get_courses_by_professor,
)



@router.get("/")
def get_courses():
    return get_all_courses()


@router.get("/{course_id}")
def get_course(course_id: int):
    return get_course_by_id(course_id)


@router.post("/")
def add_course(course: CourseCreate):
    return create_course(course)


@router.put("/{course_id}")
def edit_course(course_id: int, updated_data: dict):
    return update_course(course_id, updated_data)


@router.delete("/{course_id}")
def remove_course(course_id: int):
    return delete_course(course_id)

@router.put("/{course_id}/professor/{professor_id}")
def add_professor_to_course(course_id: int, professor_id: str):
    return assign_professor(course_id, professor_id)

@router.get("/professors/{professor_id}/courses")
def get_professor_courses(professor_id: str):
    return get_courses_by_professor(professor_id)