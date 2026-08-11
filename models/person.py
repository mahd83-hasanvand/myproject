class Person:
    def __init__(self, name_first, name_last):
        self.name_first = name_first
        self.name_last = name_last

    def get_full_name(self):
        return f"{self.name_first} {self.name_last}"

    def to_dict(self):
        return {
            "name_first": self.name_first,
            "name_last": self.name_last
        }