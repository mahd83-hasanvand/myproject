class Course:
    def __init__(
        self,
        course_id,
        title,
        code,
        unit,
        capacity
    ):
        self.course_id = course_id
        self.title = title
        self.code = code
        self.unit = unit
        self.capacity = capacity
        self.professor = None
        self.students = []

    def is_full(self):
        return len(self.students) >= self.capacity

    def add_student(self, student_id):
        if not self.is_full():
            self.students.append(student_id)

    def remove_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)

    def assign_professor(self, professor_id):
        self.professor = professor_id

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "title": self.title,
            "code": self.code,
            "unit": self.unit,
            "capacity": self.capacity,
            "professor": self.professor,
            "students": self.students
        }