# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

number = int(input(
    "Введите число, обозначающее диапазон генерирования случайных чисел для списка от -N до N: "))


def RandomList(num):
    randomlist = []
    for i in range(0, 10):
        n = random.randint(-num, num)
        randomlist.append(n)
    return randomlist


randomList = RandomList(number)
print(f"Случайный список : {randomList}")


def SumOfElements(list_elements):
    sumOfElements = 0
    for i in range(len(list_elements)):
        if i % 2 != 0:
          sumOfElements += list_elements[i]
    return sumOfElements

print("Cумма элементов списка, стоящих на нечётной позиции :")
print(SumOfElements(randomList))
