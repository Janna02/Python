# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Введите цифру, обозначающую день недели: ")
numOfDayWeek = int(input())

def DayOfWeek(num):
    if num >= 1  and num <= 5 :
        print("нет")
    elif num > 5 and num <= 7 :
           print("да") 
    else:
        print("Ввведена цифра в неверном диапазоне. Верный от 1 до 7")
       
DayOfWeek(numOfDayWeek)        