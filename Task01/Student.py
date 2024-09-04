from Task01.FIO import FIO
from Task01.Score import Score
import csv


class Student:
    name = FIO()
    current_grade = Score(2, 5, f"Оценка должна быть целым числом от 2 до 5")
    current_score = Score(0, 100, f"Результат теста должен быть целым числом от 0 до 100")

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def __str__(self):
        used_subjects = []
        for subject in self.subjects.keys():
            if len(self.subjects[subject]["grade"]) or len(self.subjects[subject]["test_score"]):
                used_subjects.append(subject)
        result = f"Студент: {self.name}\n\r"
        result += f"Предметы: {', '.join(used_subjects)}"
        return result

    def add_grade(self, subject: str, grade: int):
        self.current_grade = grade
        if subject in self.subjects.keys():
            self.subjects[subject]["grade"].append(self.current_grade)

    def get_average_grade(self) -> float:
        grades = []
        for grades_list in self.subjects.values():
            grades.extend(grades_list["grade"])
        return sum(grades) / len(grades)

    def add_test_score(self, subject, test_score):
        self.current_score = test_score
        if subject in self.subjects.keys():
            self.subjects[subject]["test_score"].append(self.current_score)

    def get_average_test_score(self, subject):
        scores = self.subjects[subject]["test_score"]
        return sum(scores) / len(scores)


    @staticmethod
    def load_subjects(subjects_file) -> dict:
        result = dict()
        with open(subjects_file, 'r', newline='', encoding="utf-8") as f:
            fr = csv.reader(f)
            for sb in list(fr)[0]:
                result[sb] = {"grade": [], "test_score": []}
        return result

