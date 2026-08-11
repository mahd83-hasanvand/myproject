class Selection:
    def __init__(self, number_student, course_id):
        self.number_student = number_student
        self.course_id = course_id

    def to_dict(self):
        return {
            "number_student": self.number_student,
            "course_id": self.course_id
        }