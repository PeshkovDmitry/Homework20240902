from Task01.FIO import FIO
from Task01.Score import Score
from Task01.Subject import Subject


class Student:
    name = FIO()
    test_score = Score(0, 100, f"Результат теста должен быть целым числом от 0 до 100")
    subject_score = Score(2, 5, f"Оценка должна быть целым числом от 2 до 5")
    subject = Subject("./Task01/subject.csv")

    def __init__(self, name):
        self.name = name
        self.subjects = {}


