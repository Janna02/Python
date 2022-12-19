# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06

import math

n = int(input("Введите число: "))

def CountNum(num):
    counted = (1 + 1/num)**num
    return counted

def ShowCountedNum(num):
    list = []
    j = 1
    for i in range(num):
        countedNum = round(CountNum(j), 2)
        j += 1
        list.append(countedNum)
    return list

def SumOfCountedNum(list_num):
    sum = math.fsum(list_num)
    return sum


showCountedNum = ShowCountedNum(n)

print(f'Для N = {n}: {showCountedNum}')

sumOfCountedNum = SumOfCountedNum(showCountedNum)
print(f'Сумма: {sumOfCountedNum}')
