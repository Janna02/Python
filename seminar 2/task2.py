# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число: "))

def MultiplicationOfNum(num):
    list = []
    for i in range(1, n+1):
        multiNumber = 1
        for j in range(1, i+1):
          multiNumber *= j
        list.append(multiNumber)
    print(list)

print(f"Произведения чисел от 1 до {n}: ")
MultiplicationOfNum(n)



