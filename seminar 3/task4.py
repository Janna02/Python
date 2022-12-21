# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("Введите целое число: "))

def DecToBin(num):
    decToBinNum = ''
    while num > 0:
         decToBinNum += str(num % 2)
         num //= 2
    print(decToBinNum)

print(f"Из десятичного числа в двоичное:") 
DecToBin(n)
