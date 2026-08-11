from models.person import Person


class Professor(Person):
    def __init__(
        self,
        name_first,
        name_last,
        code_personnel,
        department
    ):
        super().__init__(name_first, name_last)

        self.code_personnel = code_personnel
        self.department = department
        self.courses = []

    def course_assign(self, course):
        self.courses.append(course)

    def courses_get(self):
        return self.courses

    def to_dict(self):
        return {
            "name_first": self.name_first,
            "name_last": self.name_last,
            "code_personnel": self.code_personnel,
            "department": self.department,
            "courses": self.courses
        }