def import_data(data, flag):
    if flag == 3:
        with open('Data_type1.txt', 'a', encoding ='utf-8') as file1:
            for el in data:
                file1.writelines(f'{el}\n')
            file1.write('-------- \n')
    if flag == 2:
        with open('Data_type2.txt', 'a', encoding ='utf-8') as file2:
            for el in data:
                file2.write(f'{el};')
            file2.write('\n') 