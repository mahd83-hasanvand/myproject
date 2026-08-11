from models.schemas.services.data.storage import save_professors, load_professors
professors = load_professors()
def get_all_professors():
    return professors


def create_professor(professor):
    if hasattr(professor, "dict"):
        professor = professor.dict()

    professors.append(professor)
    save_professors(professors)
    return professor


def get_professor_by_id(code_personnel):
    for professor in professors:
        if professor["code_personnel"] == code_personnel:
            return professor
    return None


def update_professor(code_personnel, updated_data):
    if hasattr(updated_data, "dict"):
        updated_data = updated_data.dict(exclude_unset=True)

    for professor in professors:
        if professor["code_personnel"] == code_personnel:

            professor["name_first"] = updated_data.get(
                "name_first",
                professor["name_first"]
            )

            professor["name_last"] = updated_data.get(
                "name_last",
                professor["name_last"]
            )

            professor["code_personnel"] = updated_data.get(
                "code_personnel",
                professor["code_personnel"]
            )

            professor["department"] = updated_data.get(
                "department",
                professor["department"]
            )

            save_professors(professors)
            return professor

    return None


def delete_professor(code_personnel):
    global professors

    professors = [
        professor
        for professor in professors
        if professor["code_personnel"] != code_personnel
    ]

    save_professors(professors)
    return {"message": "Professor deleted"}