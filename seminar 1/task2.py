# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

list_for_check = [0,1]

for x in list_for_check:
    for y in list_for_check:
        for z in list_for_check:
            if (not(x or y or z)) == (not x and not y and not z):
                print(f'{x,y,z} - Выражение истинно')
            else:
                print(f'{x,y,z} - Выражение ложно')