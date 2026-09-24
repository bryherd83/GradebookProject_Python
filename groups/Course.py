class Course:
    _name = ""
    _description = ""
    _credits = 3
    _semester = "FA"

    _pre_requisites = []
    _restrictions = []
    _attributes = []

    def __init__(self, crn: str, name: str, subject: str, course_number) -> None:
        self.name = name
        self.crn = crn
        self.subject = subject
        self.course_number = course_number

