# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число N: "))
i = 2
while i <= number:
    if number % i == 0:
        number /=i
        print(i, end=" ")
    else:
        i += 1