from models.schemas.services.data.storage import save_students, load_students

students = load_students()

print(students)
print(type(students[0]))

def create_student(student):
    if hasattr(student, "dict"):
        student = student.dict()

    students.append(student)
    save_students(students)
    return student

def get_all_students():
    return students

def get_student_by_id(student_id):
    for student in students:
        if student["number_student"] == student_id:
            return student
    return None
def update_student(student_id, updated_data):
    updated_data = updated_data

    for student in students:
        if student["number_student"] == student_id:
            student["name_first"] = updated_data.get("name_first", student["name_first"])
            student["name_last"] = updated_data.get("name_last", student["name_last"])
            student["number_student"] = updated_data.get("number_student", student["number_student"])
            student["major"] = updated_data.get("major", student["major"])
            save_students(students)
            return student

    return None


def delete_student(student_id):
    global students

    students = [
        student
        for student in students
        if student["number_student"] != student_id
    ]

    save_students(students)
    return True