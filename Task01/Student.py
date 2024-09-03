from Task01.FIO import FIO
from Task01.Score import Score
import csv


class Student:
    name = FIO()
    # test_score = Score(0, 100, f"Результат теста должен быть целым числом от 0 до 100")
    # subject_score = Score(2, 5, f"Оценка должна быть целым числом от 2 до 5")

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def __str__(self):
        result = f"Студент: {self.name}\n\r"
        result += f"Предметы: {', '.join(self.subjects.keys())}"
        return result

    def add_grade(self, subject: str, grade: int):
        g = Score(2, 5, f"Оценка должна быть целым числом от 2 до 5")
        g = grade
        if subject in self.subjects.keys():
            self.subjects[subject]["grade"].append(g)

    def get_average_grade(self) -> float:
        grades = []
        for grades_list in self.subjects.values():
            grades.extend(grades_list["grade"])
        return sum(grades) / len(grades)




    @staticmethod
    def load_subjects(subjects_file) -> dict:
        result = dict()
        with open(subjects_file, 'r', newline='', encoding="utf-8") as f:
            fr = csv.reader(f)
            for sb in list(fr)[0]:
                result[sb] = {"grade": [], "test_score": []}
        return result

