import csv

class Subject:

    def __init__(self, filename: str):
        with open(filename, 'r', newline='', encoding="utf-8") as f:
            fr = csv.reader(f)
            self._subject_list = list(fr)

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value: str):
        if all([s.isalpha() and s.istitle() for s in value.split()]):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)