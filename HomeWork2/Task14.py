# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите n: "))
temp = 1
i = 1

while temp<=n:
    print(temp)
    temp = 2**i
    i += 1