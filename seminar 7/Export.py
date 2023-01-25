def export_data():
    with open('Data_type2.txt', 'r', encoding ='utf-8') as file:
        data = [i.split("; ") for i in file.read().strip().split("\n")]
        for i in data:
            for j in i:
                print(f'{j}', end='')
            print('\n')