import Data_work


def add_student():
    surname = input("Введите Фамилию: ")
    name = input("Введите имя: ")
    group = input("Введите класс: ")
    Data_work.add_student([surname, name, group])


def add_score():
    last_name = input("Введите фамилию ученика: ")
    subject = input("Введите предмет: ")
    score = input("Введите оценку или оценки через пробел: ").split()
    Data_work.add_score(last_name, subject, score)

def show_students_data():
    Data_work.get_students()


