# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите число элементов в случайном списке: "))
list_num = [random.randint(-n,n) for i in range(n)]
print(list_num)

lengthOfListEven = len(list_num)//2
lengthOfListOdd = len(list_num)//2 + 1

def Multiplication(list_elem): 
    lengthOfList = None
    if len(list_elem) % 2 != 0:
       lengthOfList = lengthOfListOdd
    else: 
        lengthOfList = lengthOfListEven

    list_milti = [list_elem[i]*list_elem[len(list_elem)-i-1] for i in range(lengthOfList)]
    print(f"Произведение пар чисел списка: ",list_milti)

Multiplication(list_num)