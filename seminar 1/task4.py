# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print("Введите номер четверти плоскости: ")
NumberOfQuarter = int(input())
def TermsOfNumberQuarter(num):
    if num == 1:
        print("x > 0 and y > 0")
    elif  num == 2:
        print("x < 0 and y > 0")   
    elif  num == 3:
        print("x < 0 and y < 0")
    elif  num == 4:
        print("x > 0 and y < 0") 
print("Диапазон возможных координат точек в  четверти: ")
TermsOfNumberQuarter(NumberOfQuarter)

