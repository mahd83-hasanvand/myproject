import json

def save_students(students):
    data = []

    for student in students:
        if isinstance(student, dict):
            data.append(student)
        else:
            data.append({
                "name_first": student.name_first,
                "name_last": student.name_last,
                "number_student": student.number_student,
                "major": student.major
            })

    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_professors(professors):
    data = []

    for professor in professors:
        data.append({
    "name_first": professor["name_first"],
    "name_last": professor["name_last"],
    "code_personnel": professor["code_personnel"],
    "department": professor["department"]
})

    with open("professors.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
def load_professors():
    try:
        with open("professors.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def load_students():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_courses(courses):
    data = []

    for course in courses:
        data.append(course)

    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_courses():
    try:
        with open("courses.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_selections(selections):
    import json

    with open("selections.json", "w", encoding="utf-8") as file:
        json.dump(selections, file, ensure_ascii=False, indent=4)


def load_selections():
    import json
    import os

    if not os.path.exists("selections.json"):
        return []

    with open("selections.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data
