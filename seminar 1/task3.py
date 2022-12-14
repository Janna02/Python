# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Введите координату x ")
x = int(input())
print("Введите координату y")
y = int(input())
def NumberOfQuarter(numOne, numTwo):
    if numOne > 0 and numTwo > 0:
        print("1")
    elif  numOne < 0 and numTwo > 0:
        print("2")   
    elif  numOne < 0 and numTwo < 0:
        print("3")
    elif  numOne > 0 and numTwo < 0:
        print("4") 
    elif  numOne == 0 and numTwo == 0:
        print("Точка на пересечении осей, не относится к четвертям плоскости")  
NumberOfQuarter(x,y)  
               