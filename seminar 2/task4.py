# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

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

with open('file.txt', 'w') as data:
 data.write('0\n')
 data.write('1\n')
 data.write('2\n')

path = 'file.txt'

def ReadPositions(path_file):
    data = open(path_file, 'r')
    dlist = [int(i.strip()) for i in data]
    data.close
    return dlist


readPositions = ReadPositions(path)

print(f"Позиции в файле: {readPositions}")


def Multiplication(list_positions, random_list):
    multiplation = 1
    for i in list_positions:
        multiplation *= random_list[i]
    return multiplation


multiplicationPositionsinFile = Multiplication(readPositions, randomList)
print(f"Произведение элементов на указанных позициях в файле: {multiplicationPositionsinFile}")

