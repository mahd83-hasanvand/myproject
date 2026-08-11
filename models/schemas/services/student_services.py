from data.storage import save_students
students = []
def get_all_students():
    return students
def create_student(student):
    students.append(student)
    save_students(students)
    return student
def get_student_by_id(student_id):
    for student in students:
        if student.number_student == student_id:
            return student
    return None
def update_student(student_id, updated_data):
    updated_data = updated_data.dict(exclude_unset=True)
    for student in students:
     if student["number_student"] == student_id:
        student["name_first"] = updated_data.get("name_first", student["name_first"])
        student["name_last"] = updated_data.get("name_last", student["name_last"])
        student["major"] = updated_data.get("major", student["major"])
        return student
    return None
def delete_student(student_id):
    global students

    students = [
        student
        for student in students
        if student.number_student != student_id 
        ]

    return True