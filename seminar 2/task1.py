# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

#  - 6782 -> 23
#  - 0,56 -> 11

input_num = float(input("Введите целое число или вещественное через точку: "))

def SumOfNum(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(f"Сумма цифр числа = {SumOfNum(input_num)}")
