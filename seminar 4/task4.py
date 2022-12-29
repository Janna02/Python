# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

k = int(input("Введите натуральную степень k: "))
list = []
for i in range(k, 0, -1):
    numForX = randint(0, 101)
    if numForX == 0:
        continue
    elif numForX == 1:
        list.append('')
    else:
        list.append(f'{numForX}*x^{i}' if i != 1 else f'{numForX}*x')
list.append(f'{randint(0, 101)}')

with open ('file.txt', 'w') as data:
    data.write(" + ".join(list) + "")