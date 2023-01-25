import Input, Import, Export


def button_click():

    print("Добро пожаловать! Выберете действие: \n",
        "Нажмите 1 - для записи данных\n",
        "Нажмите 0 - для чтения данных")
    choice = int(input())
    if choice == 1:
        flag = int(input("Нажмите 2 - для записи данных в строку\n"
                         "Нажмите 3 - для записи данных в колонку \n"))
        data = Input.input_data()
        Import.import_data(data, flag)
    if choice == 0:
        Export.export_data()
    print('Хотите завершить работу? Да/Нет')
    end = input().lower()
    if end == 'да':
        return
    if end == 'нет':
        button_click()