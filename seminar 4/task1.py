# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from math import pi

d = int(input("Задайте точность округления числа пи в в формате (1 для округления до 1 знака после запятой) : "))
print(f'Число Пи с заданной точностью {d} равно {round(pi, d)}')

