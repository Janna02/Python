import teacher_UI
import student_UI
from Data_work import load_data, save_data


def controller():
    load_data()
    print("Выберите действие: \nУчитель: 1 \nУченик: 2")
    action = input()
    if action == "1":
        choice = 1
        while choice == 1:
            print("Введите действие: \nДобавить ученика: 1 \n"
                  "Добавить оценку: 2 \n"
                  "Показать все данные по ученикам: 3\n"
                  "Выйти: 4 \n")
            action = input()
            if action == '1':
                teacher_UI.add_student()
            if action == '2':
                teacher_UI.add_score()
            if action =='3':
                teacher_UI.show_students_data()
            if action == '4':
                choice = 0
            
        else:
            save_data()
            controller()
    elif action == "2":
        choice = 1
        while choice == 1:
            last_name = input(
                'Введите фамилию ученика \n0 для выхода из программы\n')
            if last_name == '0':
                choice = 0
            else:
                student_UI.see_result(last_name)
        controller()
    else:
        print("Неверный ввод! Попробуйте еще раз.")
        controller()
