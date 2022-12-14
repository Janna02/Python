# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print("Введите координату x первой точки")
x1 = int(input())
print("Введите координату y первой точки")
y1 = int(input())
print("Введите координату x второй точки")
x2 = int(input())
print("Введите координату y второй точки")
y2 = int(input())

def DistanceOfPoints(xOne, yOne,xTwo,yTwo):
   distance = ((xTwo - xOne) ** 2 + (yTwo - yOne) ** 2) ** (0.5)
   return distance

print("Расстояние между первой и второй точками  в 2D пространстве:")
distanceOfPoints = DistanceOfPoints(x1,y1,x2,y2)
print(distanceOfPoints)
