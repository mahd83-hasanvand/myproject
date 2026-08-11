from models.schemas.services.data.storage import save_selections, load_selections
from models.services.course_services import get_all_courses

selections = load_selections()
def create_selection(selection):
    if hasattr(selection, "dict"):
        selection = selection.dict()

    selections.append(selection)
    save_selections(selections)

    courses = get_all_courses()

    for course in courses:
        if course["course_id"] == selection["course_id"]:
            if "students" not in course:
                course["students"] = []

            if selection["number_student"] not in course["students"]:
                course["students"].append(selection["number_student"])

    from models.schemas.services.data.storage import save_courses
    save_courses(courses)

    return selection


def delete_selection(number_student, course_id):
    global selections

    selections = [
        selection
        for selection in selections
        if not (
            selection["number_student"] == number_student
            and selection["course_id"] == course_id
        )
    ]

    save_selections(selections)

    return {"message": "Selection deleted"}


def get_student_courses(number_student):
    result = []

    courses = get_all_courses()

    for selection in selections:
        if selection["number_student"] == number_student:
            for course in courses:
                if course["course_id"] == selection["course_id"]:
                    result.append(course)

    return result
def get_student_courses(number_student):
    result = []

    courses = get_all_courses()

    for selection in selections:
        if selection["number_student"] == number_student:
            for course in courses:
                if course["course_id"] == selection["course_id"]:
                    result.append(course)

    return result


def get_all_selections():
    return selections