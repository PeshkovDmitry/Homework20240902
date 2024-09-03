from Task01.Student import Student


student = Student("Иван Иванов", "subject.csv")
student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)
student.add_grade("История", 5)
# student.add_test_score("История", 92)
average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")
print(student)
