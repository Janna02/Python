# Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

list = [int(i) for i in input("Введите числа через пробел: ").split()]
for i in list:
    if list.count(i) == 1:
        print(i, end = ' ')