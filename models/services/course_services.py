from models.schemas.services.data.storage import save_courses, load_courses

courses = load_courses()


def get_all_courses():
    return courses


def create_course(course):
    if hasattr(course, "dict"):
        course = course.dict()

    courses.append(course)
    save_courses(courses)
    return course


def get_course_by_id(course_id):
    for course in courses:
        if course["course_id"] == course_id:
            return course
    return None


def assign_professor(course_id, professor_id):
    course = get_course_by_id(course_id)

    if course is None:
        return {"message": "Course not found"}

    course["professor"] = professor_id
    save_courses(courses)

    return course


def update_course(course_id, updated_data):
    if hasattr(updated_data, "dict"):
        updated_data = updated_data.dict(exclude_unset=True)

    for course in courses:
        if course["course_id"] == course_id:

            course["title"] = updated_data.get(
                "title",
                course["title"]
            )

            course["code"] = updated_data.get(
                "code",
                course["code"]
            )

            course["unit"] = updated_data.get(
                "unit",
                course["unit"]
            )

            course["capacity"] = updated_data.get(
                "capacity",
                course["capacity"]
            )

            save_courses(courses)
            return course

    return None


def delete_course(course_id):
    global courses

    courses = [
        course
        for course in courses
        if course["course_id"] != course_id
    ]

    save_courses(courses)
    return {"message": "Course deleted"}


def get_courses_by_professor(professor_id):
    result = []

    for course in courses:
        if course["professor"] == professor_id:
            result.append(course)

    return result