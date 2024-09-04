from Task02.Age import Age
from Task02.Email import Email
from Task02.Name import Name


class Person:

    name = Name()
    age = Age()
    email = Email()

    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
