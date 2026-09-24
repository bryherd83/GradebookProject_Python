class Major:
    _name = ""
    _description = ""
    _career_path = []
    _minor = False
    _department = ""
    _contacts = []
    _avg_salary = 0

    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description