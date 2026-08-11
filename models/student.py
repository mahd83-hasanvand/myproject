from models.person import Person


class Student(Person):
    def __init__(
        self,
        national_id,
        name_first,
        name_last,
        number_student,
        major
    ):
        super().__init__(national_id, name_first, name_last)

        self.number_student = number_student
        self.major = major
        self.courses_selected = []

    def course_select(self, course):
        self.courses_selected.append(course)

    def course_drop(self, course):
        if course in self.courses_selected:
            self.courses_selected.remove(course)

    def courses_get(self):
        return self.courses_selected

    def to_dict(self):
        return {
            "national_id": self.national_id,
            "name_first": self.name_first,
            "name_last": self.name_last,
            "number_student": self.number_student,
            "major": self.major,
            "courses_selected": self.courses_selected
        }