import uuid
from datetime import date


class Assessment:
    id = uuid.uuid4()
    __possible_score = 0

    def __init__(self, name: str, score: int):
        """
        Setup the new Assessment object to be added to gradebook.
        :param name: Assessment Name
        :param score: Your score (default is out of 100)
        """
        self.name = name
        if score >= 0:
            self.__student_score = score
        else:
            self.__student_score = 0
        self.exam_date = date.today()

    @property
    def student_score(self) -> int:
        return self.__student_score

    @student_score.setter
    def student_score(self, value: int):
        self.__student_score = value

    @property
    def possible_score(self) -> int:
        return self.__possible_score

    @possible_score.setter
    def possible_score(self, value: int):
        if value >= 0:
            self.__possible_score = value

    def score(self) -> float:
        return self.__student_score / self.__possible_score